// 덧셈으로 이루어진 다항식이 매개변수
// 동류항끼리 더한 값을 문자열로 return
// 정수, x, + 기호로만 이루어져있다.

function solution(polynomial) {
  let xNum = 0; // x항의 상수
  let num = 0; // 상수항

  // x가 포함되는지 확인하는 함수
  const isX = (a) => {
    const regExp = /x/;
    return regExp.test(a) ? true : false;
  };

  // 문자열을 배열로 변경
  const arr = polynomial.split(" ");

  for (const a of arr) {
    // x가 포함되어 있다면
    if (isX(a)) {
      // 만약 계수가 1이라면
      if (a[0] === "x") {
        xNum += 1;
      } else {
        // 계수가 1이 아니라면
        xNum += +a.split("x")[0];
      }
      // 숫자라면
    } else {
      if (a !== "+") {
        num += +a;
      }
    }
  }

  // 결과값
  if (xNum && num) {
    if (xNum === 1) {
      return `x + ${num}`;
    } else if (xNum) {
      return `${xNum}x + ${num}`;
    }
  } else if (!num) {
    if (xNum === 1) {
      return `x`;
    } else if (xNum) {
      return `${xNum}x`;
    } else {
      return "0";
    }
  } else if (!xNum) {
    return `${num}`;
  }
}

console.log(solution("10x + 2x"));
