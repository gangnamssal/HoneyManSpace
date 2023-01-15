// 분수를 소수로 고칠 때
// 유한소수로 나타낼 수 있는 분수인지 판별
// 조건 : 기약분수로 나타내었을 때, 분모의 소인수가
// 2와 5만 존재해야 한다.
// 두 정수 a,b가 매개변수로 주어진다.
// 유한소수 : 1, 무한소수: 2를 return

function solution(a, b) {
  let cnt = 0;
  // a가 더 큰 경우
  function func1(a, b) {
    cnt = b;
    // a와 b가 기약분수가 될 때까지 while문을 반복
    while (cnt !== 1) {
      if (a % cnt === 0 && b % cnt === 0) {
        a /= cnt;
        b /= cnt;
      } else {
        cnt -= 1;
      }
    }
    // 분모가 1인 경우 무조건 유한소수
    if (b === 1) {
      return 1;
    }
    // b가 1이 아닌 경우 2와 5가 아닌 수로 나누었을 때 나머지가 0인지 체크
    for (let i = 3; i <= b; i++) {
      if (i !== 5 && i % 2 !== 0 && i % 5 !== 0 && b % i === 0) {
        return 2;
      }
    }
    return 1;
  }
  // b가 더 큰 경우
  function func2(a, b) {
    cnt = a;
    // a와 b가 기약분수가 될 때까지 while문을 반복
    while (cnt !== 1) {
      if (a % cnt === 0 && b % cnt === 0) {
        a /= cnt;
        b /= cnt;
      } else {
        cnt -= 1;
      }
    }
    // b가 1이 아닌 경우 2와 5가 아닌 수로 나누었을 때 나머지가 0인지 체크
    for (let i = 3; i <= b; i++) {
      if (i !== 5 && i % 2 !== 0 && i % 5 !== 0 && b % i === 0) {
        return 2;
      }
    }
    return 1;
  }
  // a와 b의 크기를 비교
  return a > b ? func1(a, b) : func2(a, b);
}
