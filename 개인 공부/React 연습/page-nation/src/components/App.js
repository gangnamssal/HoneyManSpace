import { HashRouter as Router, Routes, Route } from "react-router-dom";
import PageNation from "../routes/PageNation";
import PageNationItem from "../routes/PageNationItem";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" exact element={<PageNation />}></Route>
          <Route path="/item/:id" element={<PageNationItem />}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
