// 분수를 소수로 고칠 때
// 유한소수로 나타낼 수 있는 분수인지 판별
// 조건 : 기약분수로 나타내었을 때, 분모의 소인수가
// 2와 5만 존재해야 한다.
// 두 정수 a,b가 매개변수로 주어진다.
// 유한소수 : 1, 무한소수: 2를 return

function solution(a, b) {
  if (a > b) {
    while (true) {
      if (b === 1) {
        return 1;
      } else if (a % b !== 0) {
        b -= 1;
      } else {
        return b % 2 === 0 || b % 5 === 0 || b % 10 === 0 ? 1 : 2;
      }
    }
  } else if (a === b) {
    return 1;
  } else {
    while (true) {
      if (b % a !== 0) {
        a -= 1;
      } else {
        return a % 2 === 0 || a % 5 === 0 || a % 10 ? 1 : 2;
      }
    }
  }
}
