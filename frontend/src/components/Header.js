import React from "react";
import { Link } from "react-router-dom";
import "../components/style/header.css";

export const Header = () => {
  return (
    <>
      <div className="Header_container" >
          <ul className="navbar_container">
            <li className="title" ><Link to="/">Cross Share</Link></li>
            <li className="nav_elements"><Link to="/contact">Contact</Link></li>
            <li className="nav_elements"><Link to="/about">About</Link></li>
          </ul>
      </div>
    </>
  );
};
