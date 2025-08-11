import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './Meters.css';

function Meters() {
  const { substationName } = useParams();
  const [meters, setMeters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMeters = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch(
          `http://localhost:5000/api/meters/${encodeURIComponent(substationName)}`
        );
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.status === 'success') {
          setMeters(Array.isArray(data.meters) ? data.meters : []);
        } else {
          throw new Error(data.message || 'Failed to fetch meters');
        }
      } catch (err) {
        console.error('Error fetching meters:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchMeters();
  }, [substationName]);

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Loading meters...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error">
        <p>Error: {error}</p>
        <button onClick={() => window.location.reload()}>Retry</button>
      </div>
    );
  }

  return (
    <div className="meters-container">
      <h2>{substationName}</h2>
      <div className="meters-list">
        {meters.length > 0 ? (
          meters.map((meter, index) => (
            <div 
              key={index}
              className="meter-card"
              onClick={() => {
                navigate(`/meter/${encodeURIComponent(substationName)}/${encodeURIComponent(meter.name)}/${meter.slave_id}`);
              }}
            >
              <h3>{meter.name}</h3>
              <p>Slave ID: {meter.slave_id}</p>
            </div>
          ))
        ) : (
          <div className="no-meters">
            <p>No meters found for this substation</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Meters;