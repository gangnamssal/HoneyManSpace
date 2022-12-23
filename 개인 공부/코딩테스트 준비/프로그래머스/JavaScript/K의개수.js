// 정수 i, j, k가 매개변수로 주어진다.
// i부터 j까지 k가 몇 번 등장하는지 return

function solution(i, j, k) {
  let result = 0; // 결과값

  // 1. for문을 이용해 i ~ j + 1까지 수를 반복
  for (let start = i; start < j + 1; start++) {
    const strStart = start + ""; // 수를 문자열로 변경

    // // 2. 문자열을 순회하면서 k와 같은 문자가 있으면 result를 1증가
    // for (const str of strStart) {
    //   str === String(k) ? result++ : null;
    // }
    [...strStart].forEach((str) => {
      str === String(k) ? result++ : null;
    });
  }

  return result;
}
