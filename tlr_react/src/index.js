import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';

// import { BrowserRouter as Router, Route } from "react-router-dom";
// import Header from './components/Header';
// import GoalDashboard from './components/GoalDashboard';
// import Goal1 from './components/Goal1'

ReactDOM.render(
  // <Router>
  // <Route exact path="/home" component={GoalDashboard} />
  // <Route exact path="/goal-details" component={GoalDetails} />
  // </Router>,

  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
