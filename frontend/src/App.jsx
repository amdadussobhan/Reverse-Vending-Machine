import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import './App.css';

const App = () => {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>

      </Routes>
    </BrowserRouter>
  );
}

export default App;