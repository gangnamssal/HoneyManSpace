/**
    1. 현재 값보다 앞에 있는 배열을 검사하면서 현재 값의 위치를 정한다.
    2. 위치를 정했으면 그 자리에 값을 삽입한다.
 */

function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let currentVal = arr[i];
    let currentIdx = i;
    for (let j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
      arr[j + 1] = arr[j];
      currentIdx = j;
    }
    arr[currentIdx] = currentVal;
  }
  return arr;
}

console.log(insertionSort([123, 23, 4, 43, 45, 2, 3, 64, 45, 4, 3, 6, 89, 0]));
