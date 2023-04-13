// 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야한다.
// 삼각형의 두 변의 길이가 담긴 배열이 매개변수
// 나머지 한 변이 될 수 있는 정수의 개수를 return

function solution(slides) {
  // slides 내 최댓값
  let currentMax = Math.max(...slides);
  // slides 내 최솟값
  let currentMin = Math.min(...slides);
  // 추가로 들어오는 값
  let extraNum = 1;
  // 결과
  let result = 0;
  // 두 가지의 경우로 나눈다
  // 1. slides 안에 있는 두 변 중 큰 값이 최대인 경우
  while (extraNum <= currentMax) {
    if (currentMax >= extraNum + currentMin) {
      extraNum++;
    } else {
      extraNum++;
      result++;
    }
  }
  extraNum = currentMax + 1;
  // 2. slides 안에 있는 두 변보다 큰 값이 들어온 경우
  while (extraNum < currentMax + currentMin) {
    if (extraNum < currentMax + currentMin) {
      result++;
      extraNum++;
    }
  }
  return result;
}

console.log(solution([11, 7]));
