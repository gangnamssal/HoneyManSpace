/**
 * 1. 주어진 인덱스 번호에 수를 추출하는 함수를 만든다.
 * 2. 주어진 숫자의 길이를 구하는 함수를 만든다.
 * 3. 기수 정렬을 수행하는 함수를 만든다.
 */

/**
 *
 * @param {number} num 배열의 현재 수를 받는다.
 * @param {number} idx 구하고 싶은 인덱스 번호를 받는다. (오른쪽부터 0)
 * @returns 구하고 싶은 인덱스 번호의 수가 나온다.
 */
function getDigit(num, idx) {
  return Math.floor(Math.abs(num) / Math.pow(10, idx)) % 10;
}

/**
 *
 * @param {number} num 배열의 현재 수를 받는다.
 * @returns 현재 수의 길이를 반환한다.
 */
function moseDigit(num) {
  return Math.ceil(Math.log10(Math.abs(num)));
}

/**
 *
 * @param {Array} arr 정렬되지 않는 배열을 받는다.
 * @returns 배열 내에서 가장 긴 수의 길이를 return한다.
 */
function mostLengthArr(arr) {
  let maxIdx = 0;
  arr.forEach((item) => {
    moseDigit(item) > maxIdx ? (maxIdx = moseDigit(item)) : null;
  });
  return maxIdx;
}

function radixSort(arr) {
  for (let i = 0; i < mostLengthArr(arr); i++) {
    const result = Array.from({ length: 10 }, () => []);
    arr.forEach((item) => {
      const digitNum = getDigit(item, i);
      result[digitNum].push(item);
    });
    arr = [].concat(...result);
  }

  return arr;
}

console.log(
  radixSort([
    123, 234, 23, 21, 6, 4, 2, 7547, 54324, 56423543, 43, 534, 1233, 1,
  ])
);
