import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    console.log({ email, password });
    // Add your login API logic here
  };

  return (
    <div className="flex flex-box items-center justify-center min-h-screen bg-white-800">
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-3xl font-bold text-center text-gray-900">Login</h2>
        <form onSubmit={handleLogin} className="space-y-6">
          <div className="flex flex-col space-y-2">
            <label htmlFor="email" className="text-sm font-medium text-gray-700">Email</label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 text-gray-900 bg-gray-200 border rounded-md focus:border-blue-500 focus:ring-blue-500 focus:outline-none"
            />
          </div>
          <div className="flex flex-col space-y-2">
            <label htmlFor="password" className="text-sm font-medium text-gray-700">Password</label>
            <input
              id="password"
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-3 text-gray-900 bg-gray-200 border rounded-md focus:border-blue-500 focus:ring-blue-500 focus:outline-none"
            />
          </div>
          <button type="submit" className="w-full p-3 text-sm font-bold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
            Login
          </button>
        </form>
        <p className="mt-4 text-sm text-center text-gray-400">
          Don't have an account? <Link to="/signup" className="text-blue-500 hover:text-blue-600 focus:outline-none focus:underline">Sign up here</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
