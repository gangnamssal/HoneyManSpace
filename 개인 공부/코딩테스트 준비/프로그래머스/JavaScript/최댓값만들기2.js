// 정수 배열이 매개변수
// 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return

function solution(numbers) {
  // 배열을 정렬한 뒤 배열의 맨 앞 2개의 요소와
  // 맨 뒤 2개의 요소를 곱한 값을 비교하는 로직
  const newNumbers = numbers.sort((a, b) => a - b);
  const LENGTH = numbers.length;

  if (
    newNumbers[0] * newNumbers[1] >
    newNumbers[LENGTH - 1] * newNumbers[LENGTH - 2]
  ) {
    return newNumbers[0] * newNumbers[1];
  } else {
    return newNumbers[LENGTH - 1] * newNumbers[LENGTH - 2];
  }
}
