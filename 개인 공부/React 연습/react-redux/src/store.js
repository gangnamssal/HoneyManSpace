import { createStore } from "redux";

const ADD = "ADD";
const DELETE = "DELETE";

const addToDo = (text) => {
  store.dispatch({
    type: ADD,
    text,
  });
};

const deleteToDo = (id) => {
  store.dispatch({
    type: DELETE,
    id: parseInt(id),
  });
};

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD:
      return [{ text: action.text, id: Date.now() }, ...state];
    case DELETE:
      const newState = state.filter((todo) => {
        return todo.id !== action.id;
      });
      return newState;
    default:
      return state;
  }
};

const store = createStore(reducer);

export const actionCreator = {
  addToDo,
  deleteToDo,
};

export default store;
