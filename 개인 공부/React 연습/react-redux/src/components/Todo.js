import { actionCreator } from "../store";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

function Todo({ text, onClick, id }) {
  return (
    <li>
      <Link to={`/${id}`}>
        {text}
        <button onClick={onClick}>DEL</button>
      </Link>
    </li>
  );
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    onClick() {
      dispatch(actionCreator.deleteToDo(ownProps.id));
    },
  };
};

export default connect(null, mapDispatchToProps)(Todo);
