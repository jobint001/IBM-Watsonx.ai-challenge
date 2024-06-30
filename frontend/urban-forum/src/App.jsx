import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';  // Make sure to import your Navbar
import HomePage from './pages/HomePage';
import Signup from './components/Signup';
import LoginPage from './components/Login';
import { MenuProvider } from './context/MenuContext';

function App() {
  return (
    <MenuProvider>
      <Router>
        <Navbar />  {/* Navbar is placed outside the Routes but inside the Router */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Router>
    </MenuProvider>
  );
}

export default App;
