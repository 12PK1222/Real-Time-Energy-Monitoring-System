import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Substations from './pages/Substations';
import Meters from './pages/Meters';
import MeterDetail from './pages/MeterDetail';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="app-body">
          <Sidebar />
          <div className="app-content">
            <Routes>
              <Route path="/" element={<Substations />} />
              <Route path="/substations/:substationName" element={<Meters />} />
              <Route path="/meter/:substationName/:meterName/:slaveId" element={<MeterDetail />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;