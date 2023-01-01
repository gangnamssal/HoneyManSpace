// 정수 n을 기준으로 n과 가까운 수부터 정렬
// n과 거리가 같다면 더 큰 수를 앞에 오도록 배치
// 정수가 담긴 배열 numlist와 정수n
// numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열 return

function solution(numlist, n) {
  // numlist를 순회하면서 n과의 거리를 저장한다.
  numlist.forEach((item, index, arr) => {
    arr[index] = [item, Math.abs(item - n)];
  });

  // 저장한 뒤 2차원 배열이 된 numlist를 거리가 짧은 순으로 정렬한다.
  // 단 같은 값이면 더 큰 수를 앞으로 해서 정렬한다.
  numlist.sort((a, b) => {
    return a[1] > b[1] ? 1 : a[1] < b[1] ? -1 : a[0] > b[0] ? -1 : 1;
  });

  // 정렬된 numlist를 순회하면서 정수만 뽑아서 새로운 배열을 만든다.
  const result = numlist.map((item) => {
    return item[0];
  });
  return result;
}
