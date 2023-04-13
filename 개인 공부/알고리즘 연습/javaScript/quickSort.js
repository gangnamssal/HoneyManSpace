/**
 * 1. 피벗함수를 작성한다.
 *      1-1. 첫 번째 값을 시작 값으로 한다.
 *      1-2. 배열을 순회하면서 시작작 값보다 작은 값을 발견하면 idx를 1 증가시킨 뒤 순서를 변경한다.
 *      1-3. 순회가 끝나면 첫 번째 값과 idx 값의 순서를 변경한다.
 *      1-4. idx값을 return한다.
 * 2. 퀵 정렬을 실시한다.
 *      2-1. 피벗함수를 호출한 뒤 배열을 처음 순회한다.
 *      2-2. 재귀를 통해 다시 퀵 정렬 함수를 불러온다. 이때 왼쪽과 오른쪽으로 함수를 나누어 실시한다.
 *      2-3. 첫 배열를 return한다. (첫 배열을 계속 변경되기 때문에 마지막으로 return된 배열은 정렬되어 있다.)
 */

function pivot(arr, start = 0, end = arr.length - 1) {
  // 순서를 변경하는 함수
  const swap = (array, arr1, arr2) => {
    [array[arr1], array[arr2]] = [array[arr2], array[arr1]];
  };

  let startVal = arr[start];
  let idx = start + 1;

  for (let i = start + 1; i < arr.length; i++) {
    if (startVal >= arr[i]) {
      swap(arr, i, idx);
      idx++;
    }
  }
  swap(arr, start, idx - 1);
  return idx - 1;
}

function quickSort(arr, start = 0, end = arr.length - 1) {
  if (start < end) {
    const pivotVal = pivot(arr, start, end);
    // 왼쪽
    quickSort(arr, start, pivotVal - 1);
    // 오른쪽
    quickSort(arr, pivotVal + 1, end);
  }

  return arr;
}

console.log(quickSort([4, 8, 2, 89, 34, 451, 5, 1]));
