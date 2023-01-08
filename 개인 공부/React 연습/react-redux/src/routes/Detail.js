import React from "react";
import { useParams } from "react-router-dom";
import { connect } from "react-redux";

function Detail({ state }) {
  const id = parseInt(useParams().id);
  const detailObj = state.filter((todo) => {
    return todo.id === id;
  })[0];
  const text = detailObj.text;
  return (
    <div>
      <h1>{text}</h1>
      <h5>{id}</h5>
    </div>
  );
}

const mapStateToProps = (state) => {
  return { state };
};

export default connect(mapStateToProps)(Detail);
