import { createStore } from "redux";

const ADD = "ADD";
const addNumber = (number) => {
  return {
    type: ADD,
    number,
  };
};

const reducer = (state = 0, action) => {
  switch (action.type) {
    case ADD:
      const newState = state + 1;
      return newState;
    default:
      return state;
  }
};

const store = createStore(reducer);

export { addNumber };

export default store;
