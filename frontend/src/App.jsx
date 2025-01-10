import React from 'react';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import About from './components/About';

const App = () => {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route exact path='/' Component={Home} />
        <Route exact path='/Home' Component={Home} />
        <Route exact path='/about' Component={About} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
