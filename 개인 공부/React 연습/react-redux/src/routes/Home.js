import React from "react";
import { connect } from "react-redux";
import { useState } from "react";
import { actionCreator } from "../store";
import Todo from "../components/Todo";

function Home({ state, addTodo }) {
  console.log(state);
  const [text, setText] = useState("");
  const onChange = (event) => {
    setText(event.target.value);
  };

  const onSubmit = (event) => {
    event.preventDefault();
    setText("");
    addTodo(text);
  };
  return (
    <div>
      <h1>Todo</h1>
      <form onSubmit={onSubmit}>
        <input onChange={onChange} type="text" value={text} />
        <button>ADD</button>
      </form>
      <ul>
        {state.map((todo) => {
          return <Todo {...todo} key={todo.id} />;
        })}
      </ul>
    </div>
  );
}

const mapStateToProps = (state, ownProps) => {
  return { state };
};
const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    addTodo(text) {
      dispatch(actionCreator.addToDo(text));
    },
  };
};
export default connect(mapStateToProps, mapDispatchToProps)(Home);
