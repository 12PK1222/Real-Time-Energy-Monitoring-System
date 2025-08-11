import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="sidebar-content">
        <ul className="sidebar-menu">
          <li>
            <Link to="/">All Substations</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Sidebar;