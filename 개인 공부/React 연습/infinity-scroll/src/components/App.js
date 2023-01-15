import React from "react";
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../routes/Home";
import Detail from "../routes/Detail";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" exact element={<Home />}></Route>
          <Route path="/detail" element={<Detail />}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
