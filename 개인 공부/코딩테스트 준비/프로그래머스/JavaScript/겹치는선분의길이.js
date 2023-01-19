/**
 선분 3개가 평행
 세 선분의 시작과 끝 좌표가 들어있는 2차원 배열 lines
 두 개 이상의 선분이 겹치는 부분의 길이를 return
 */

/**
 * @param {number[]} lines
 * @returns {number[]} lines
 */
function solution(lines) {
  const result = {};
  // lines의 배열의 첫 번째 수가 낮은 순서대로 정렬
  lines.sort((a, b) => a[0] - b[0]);

  // 정렬된 배열을 순회하면서 숫자가 몇번 등장하는지 객체에 저장
  lines.forEach((item) => {
    for (let i = item[0]; i <= item[1]; i++) {
      result[i] ? result[i]++ : (result[i] = 1);
    }
  });
  console.log(lines);
  let answer = 0;
  let cnt = 0;
  // 객체를 순회하면서 개수가 2개 이상인 수를 찾으며 선분의 길이를 잰다.
  for (const [keys, values] of Object.entries(result)) {
    if (values >= 2) {
      cnt++;
    } else {
      if (cnt !== 0) {
        answer += cnt - 1;
        cnt = 0;
      }
    }
  }

  return answer;
}

console.log(
  solution([
    [0, 5],
    [1, 4],
    [2, 3],
  ])
);
