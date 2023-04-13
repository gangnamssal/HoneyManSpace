/**
    1. 병합 함수를 작성한다.    
        1-1 왼쪽 배열과 오른쪽 배열을 비교한다.
        1-2 두 배열을 정렬되어 있다.
        1-3 정렬이 끝난 뒤 남은 배열의 값을 그대로 붙인다.
    2. 정렬 함수를 작성한다.
        2-1 정렬 함수는 주어진 배열을 재귀로 반씩 나눈다.
        2-2 함수의 길이가 1보다 작게되면 나누는 과정을 중단한다.
        2-3 나누어진 왼쪽, 오른쪽 함수를 병합하는 과정을 진행한다.
 */
function merge(arr1, arr2) {
  let results = []; // 결과를 저장하는 변수
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] > arr2[j]) {
      results = [...results, arr2[j]];
      j++;
    } else {
      results = [...results, arr1[i]];
      i++;
    }
  }

  while (i < arr1.length) {
    results = [...results, arr1[i]];
    i++;
  }
  while (j < arr2.length) {
    results = [...results, arr2[j]];
    j++;
  }

  return results;
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));
  return merge(left, right);
}

console.log(
  mergeSort([
    1, 66, 9, 32, 56, 8, 45, 54, 12, 3, 4, 6, 1, 3, 5, 7, 9, 5, 65, 4, 5, 3, 4,
    3, 5, 0, 8, 567, 5, 4, 42, 32, 53,
  ])
);
