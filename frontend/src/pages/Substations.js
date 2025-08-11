import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Substations.css';

function Substations() {
  const [substations, setSubstations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchSubstations = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch('http://localhost:5000/api/substations');
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.status === 'success') {
          setSubstations(data.substations);
        } else {
          throw new Error(data.message || 'Failed to fetch substations');
        }
      } catch (error) {
        console.error('Error fetching substations:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSubstations();
  }, []);

  const filteredSubstations = substations.filter(substation =>
    substation.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>Loading substations...</p>
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
    <div className="substations-container">
      <h1>Substation Monitoring</h1>
      
      <div className="search-container">
        <input
          type="text"
          placeholder="Search substations..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <div className="substations-grid">
        {filteredSubstations.length > 0 ? (
          filteredSubstations.map((substation, index) => (
            <div 
              key={index} 
              className="substation-card"
              onClick={() => navigate(`/substations/${encodeURIComponent(substation)}`)}
            >
              <h3>{substation}</h3>
              <div className="card-footer">
                <span>Click to view meters</span>
              </div>
            </div>
          ))
        ) : (
          <div className="no-results">
            {searchTerm ? 'No matching substations found' : 'No substations available'}
          </div>
        )}
      </div>
    </div>
  );
}

export default Substations;