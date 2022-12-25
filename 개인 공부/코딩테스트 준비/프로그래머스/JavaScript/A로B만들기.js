// 문자열 before, after가 매개변수
// before의 순서를 바꾸어 after를 만들 수 있으면
// 1, 아니면 0

function solution(before, after) {
  // 1. befor의 문자들과 after 문자들을 배열로 변경 후 오름차순으로 정렬
  const beforeArr = before.split("").sort();
  const afterArr = after.split("").sort();
  let result = 1;

  // 2. 반복문을 돌면서 두 배열의 index 값이 다르면 0
  for (let n = 0; n < beforeArr.length; n++) {
    if (beforeArr[n] !== afterArr[n]) {
      result = 0;
      break;
    }
  }

  return result;
}
