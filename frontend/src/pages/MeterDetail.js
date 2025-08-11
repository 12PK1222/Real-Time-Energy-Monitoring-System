import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './MeterDetail.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function MeterDetail() {
  const { substationName, meterName, slaveId } = useParams();
  const [meterData, setMeterData] = useState(null);
  const [historyData, setHistoryData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [simulationMode, setSimulationMode] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const statusRes = await fetch(`${API_URL}/api/status`);
      const statusData = await statusRes.json();
      setSimulationMode(statusData.simulation_mode);
      
      const response = await fetch(
        `${API_URL}/api/meter-data?meter_name=${encodeURIComponent(meterName)}&slave_id=${slaveId}`
      );
      
      if (!response.ok) throw new Error('Failed to fetch data');
      
      const data = await response.json();
      
      if (data.status === 'success') {
        setMeterData(data.data);
        setHistoryData(prev => [...prev.slice(-19), {
          time: new Date().toLocaleTimeString(),
          ...data.data
        }]);
      } else {
        throw new Error(data.message || 'Invalid data received');
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000);
    return () => clearInterval(interval);
  }, [substationName, meterName, slaveId]);

  const formatValue = (value, unit = '') => {
    if (value === undefined || value === null) return '--';
    return typeof value === 'number' ? `${value.toFixed(2)} ${unit}` : value;
  };

  if (loading && !meterData) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading meter data...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <h3>Error Loading Data</h3>
        <p>{error}</p>
        <button onClick={fetchData}>Retry</button>
      </div>
    );
  }

  return (
    <div className="meter-detail">
      {simulationMode && (
        <div className="simulation-banner">
          SIMULATION MODE ACTIVE - Displaying simulated data
        </div>
      )}
      
      <div className="header">
        <h2>{meterName} (Slave ID: {slaveId})</h2>
        <h3>{substationName}</h3>
        <p className="last-updated">
          Last updated: {new Date().toLocaleTimeString()}
        </p>
      </div>

      <div className="data-grid">
        <div className="data-section voltage">
          <h4>Voltage Measurements</h4>
          <div className="value-row">
            {['Voltage Vab', 'Voltage Vbc', 'Voltage Vca'].map(param => (
              <div key={param} className="value-card">
                <span>{param}</span>
                <span className="value">
                  {formatValue(meterData?.[param], 'V')}
                  {simulationMode && <span className="simulated">simulated</span>}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="data-section current">
          <h4>Current Measurements</h4>
          <div className="value-row">
            {['IR Current', 'IY Current', 'IB Current'].map(param => (
              <div key={param} className="value-card">
                <span>{param}</span>
                <span className="value">
                  {formatValue(meterData?.[param], 'A')}
                  {simulationMode && <span className="simulated">simulated</span>}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="data-section power">
          <h4>Power Measurements</h4>
          <div className="value-row">
            {['Active Power', 'Apparent Power', 'Reactive Power'].map(param => (
              <div key={param} className="value-card">
                <span>{param}</span>
                <span className="value">
                  {formatValue(meterData?.[param], param.includes('Active') ? 'kW' : 
                   param.includes('Apparent') ? 'kVA' : 'kVAr')}
                  {simulationMode && <span className="simulated">simulated</span>}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="data-section other">
          <h4>Other Parameters</h4>
          <div className="value-row">
            {['Power Factor', 'Frequency'].map(param => (
              <div key={param} className="value-card">
                <span>{param}</span>
                <span className="value">
                  {formatValue(meterData?.[param], param === 'Frequency' ? 'Hz' : '')}
                  {simulationMode && <span className="simulated">simulated</span>}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="chart-section">
        <div className="chart-container">
          <h4>Voltage Trends</h4>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={historyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis label={{ value: 'Volts', angle: -90, position: 'insideLeft' }} />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="Voltage Vab" stroke="#8884d8" name="Vab (V)" />
              <Line type="monotone" dataKey="Voltage Vbc" stroke="#82ca9d" name="Vbc (V)" />
              <Line type="monotone" dataKey="Voltage Vca" stroke="#ffc658" name="Vca (V)" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-container">
          <h4>Power Trends</h4>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={historyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis label={{ value: 'Power', angle: -90, position: 'insideLeft' }} />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="Active Power" stroke="#8884d8" name="Active (kW)" />
              <Line type="monotone" dataKey="Apparent Power" stroke="#82ca9d" name="Apparent (kVA)" />
              <Line type="monotone" dataKey="Reactive Power" stroke="#ffc658" name="Reactive (kVAr)" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

export default MeterDetail;