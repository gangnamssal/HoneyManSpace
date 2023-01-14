import React from "react";
import { connect } from "react-redux";
import { useState } from "react";

function PageNation({ state }) {
  const [currentBtn, setCurrentBtn] = useState(1);
  const [currentPage, setCurrentPage] = useState(1);
  const getNextBtn = () => {
    if (currentBtn < state.length - 1) {
      setCurrentBtn((current) => current + 2);
    }
  };
  const getBeforeBtn = () => {
    if (currentBtn > 1) {
      setCurrentBtn((current) => current - 2);
    }
  };
  const setPage = (e) => {
    setCurrentPage(e.target.textContent);
  };
  return (
    <div>
      <h1>PageNation</h1>

      {
        <div>
          <h1>{state[currentPage - 1].text}</h1>
          <button onClick={getBeforeBtn}>이전</button>
          <button hidden={currentBtn > state.length} onClick={setPage}>
            {currentBtn}
          </button>
          <button hidden={currentBtn + 1 > state.length} onClick={setPage}>
            {currentBtn + 1}
          </button>
          <button onClick={getNextBtn}>다음</button>
        </div>
      }
    </div>
  );
}

const mapStateToProps = (state, ownProps) => {
  return { state };
};

export default connect(mapStateToProps)(PageNation);
