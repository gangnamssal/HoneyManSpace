/**
    1. 배열을 순회하면서 최솟값을 찾는다.
    2. 최솟값과 앞자리를 바꾼다.
    3. 만약 최솟값이 최초의 값이면 자리 바꾸는 것을 하지 않는다.
 */
function seletionSort(arr) {
  let result = [...arr];
  for (let i = 0; i < result.length; i++) {
    let lowest = i;
    for (let j = i + 1; j < result.length; j++) {
      if (result[lowest] > result[j]) {
        lowest = j;
      }
    }
    if (i !== lowest) {
      [result[i], result[lowest]] = [result[lowest], result[i]];
    }
  }
  return result;
}

console.log(seletionSort([4, 2, 3, 7, 45, 12, 38, 66, 4]));
