// 버블 정렬 JS 연습

/**
    1. 2개의 루프가 필요하다.
    2. 뒤에서부터 정렬을 시작한다.
    3. 만약 정렬이 되지 않았으면 바로 루프를 빠져나온다.
 */

function bubbleSort(arr) {
  const result = [...arr];

  for (let i = result.length; i > 0; i--) {
    let isDone = true;

    for (let j = 0; j < i - 1; j++) {
      if (result[j] > result[j + 1]) {
        [result[j], result[j + 1]] = [result[j + 1], result[j]];
        isDone = false;
      }
    }
    if (isDone) break;
  }
  return result;
}

console.log(bubbleSort([6, 3, 8, 0, 4, 657, 4, 53, 423, 41, 2, 312, 324, 12]));
