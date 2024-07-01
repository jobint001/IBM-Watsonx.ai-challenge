import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div>
      <h1>Welcome to the Homepage</h1>
      <Link to="/signup">Sign Up</Link>
      <br />
      <Link to="/login">Login</Link>
    </div>
  );
}

export default HomePage;
