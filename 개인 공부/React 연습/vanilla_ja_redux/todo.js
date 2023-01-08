const $root = document.getElementById("root");
const $h1 = document.createElement("h1");
const $input = document.createElement("input");
const $button = document.createElement("button");
const $ul = document.createElement("ul");
$h1.textContent = "ToDos";
$button.textContent = "ADD";

$root.appendChild($h1);
$root.appendChild($input);
$root.appendChild($button);
$root.appendChild($ul);

const ADD = "ADD";
const DELETE = "DELETE";

reducer = (todos = [], action) => {
  switch (action.type) {
    case ADD:
      return [{ text: action.text, id: Date.now() }, ...todos];
    case DELETE:
      const newTodos = todos.filter((todo) => {
        return todo.id !== action.id;
      });
      return newTodos;
    default:
      return todos;
  }
};

const store = Redux.createStore(reducer);

const onDelete = (event) => {
  const id = parseInt(event.target.parentNode.id);
  store.dispatch({ type: DELETE, id });
};

const paintTodo = (todos) => {
  todos.forEach((todo) => {
    const $li = document.createElement("li");
    const $DeleteBtn = document.createElement("button");
    $DeleteBtn.textContent = "DELETE";
    $li.id = todo.id;
    $li.textContent = todo.text;
    $ul.appendChild($li);
    $li.appendChild($DeleteBtn);
    $DeleteBtn.addEventListener("click", onDelete);
  });
};

store.subscribe(() => {
  const todos = store.getState();
  $ul.innerHTML = "";
  paintTodo(todos);
});

const addTodo = () => {
  if ($input.value === "") return;
  const inputValue = $input.value;
  $input.value = "";
  store.dispatch({ type: ADD, text: inputValue });
};

$button.addEventListener("click", addTodo);
