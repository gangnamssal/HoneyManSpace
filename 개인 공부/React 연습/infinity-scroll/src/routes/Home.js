import React from "react";
import style from "../style/Home.module.css";

function Home() {
  let number = 3;
  const toScroll = () => {
    const $div = document.querySelector(".home");
    const $el = document.createElement("div");
    $el.className = style.box;
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      number += 1;
      $el.textContent = number;
      $div.appendChild($el);
    }
  };
  window.addEventListener("scroll", toScroll);
  return (
    <div>
      <h1>Infinity Scroll</h1>
      <div className="home">
        <div className={style.box}>{0}</div>
        <br></br>
        <div className={style.box}>{1}</div>
        <br></br>
        <div className={style.box}>{2}</div>
        <br></br>
        <div className={style.box}>{3}</div>
        <br></br>
      </div>
    </div>
  );
}

export default Home;
