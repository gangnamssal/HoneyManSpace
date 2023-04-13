// 세 선분의 시작과 끝 좌표가 2차원 배열로 주어진다.
// 두 개 이상의 선분이 겹치는 부분의 길이를 return
function solution(lines) {
  const resultObj = {};
  let result = 0;
  let start;
  let end;

  lines.forEach((line) => {
    start = line[0];
    end = line[1];

    while (start !== end) {
      if (!resultObj[[start, start + 1]]) {
        resultObj[[start, start + 1]] = 1;
      } else {
        resultObj[[start, start + 1]]++;
      }
      start += 1;
    }
  });

  for (let i in resultObj) {
    if (resultObj[i] > 1) {
      result++;
    }
  }

  return result;
}

console.log(
  solution([
    [0, 1],
    [2, 5],
    [3, 9],
  ])
);
