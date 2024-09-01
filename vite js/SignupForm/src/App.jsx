import './App.css';
import React, { useState } from 'react';
import SignupForm from './components/SignupForm';
import Login from './components/Login';
import Dashboard from './components/Dashboard';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isSignedUp, setIsSignedUp] = useState(false);

  const handleSignupSuccess = () => {
    setIsSignedUp(true);
  };

  const handleLoginSuccess = () => {
    setIsLoggedIn(true);
  };

  if (isLoggedIn) {
    return (
      <div className="App">
        <h1>Dashboard</h1>
        <Dashboard />
      </div>
    );
  }

  if (isSignedUp) {
    return (
      <div className="App">
        <h1>Login</h1>
        <Login onLoginSuccess={handleLoginSuccess} />
      </div>
    );
  }

  return (
    <div className="App">
      <h1>Signup Form</h1>
      <SignupForm onSignupSuccess={handleSignupSuccess} />
    </div>
  );
}

export default App;
