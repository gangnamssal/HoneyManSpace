// 점 네 개의 좌표를 담은 이차원 배열 dots가 매개변수로 주어짐
// 주어진 네 개의 점을 두 개씩 이었을 때
// 평행이 되는 경우가 있으면 1 없으면 0을 return
// 두 직선이 겹치는 경우에도 1을 return
function solution(dots) {
  // 평행한 직선은 기울기가 동일하다.
  const dotsIdx = [0, 1, 2, 3];
  let result = 0;

  // 기울기를 계산하는 함수
  function calFnc(index1, index2) {
    const lean1 =
      Math.abs(dots[index1[0]][1] - dots[index1[1]][1]) /
      Math.abs(dots[index1[0]][0] - dots[index1[1]][0]);
    const lean2 =
      Math.abs(dots[index2[0]][1] - dots[index2[1]][1]) /
      Math.abs(dots[index2[0]][0] - dots[index2[1]][0]);

    return lean1 === lean2 ? 1 : 0;
  }

  for (let i = 1; i < dotsIdx.length; i++) {
    switch (i) {
      case 1:
        result = calFnc([0, 1], [2, 3]);
        break;
      case 2:
        result = calFnc([0, 2], [1, 3]);
        break;
      case 3:
        result = calFnc([0, 3], [1, 2]);
        break;
      default:
        break;
    }
    if (result) {
      return result;
    }
  }

  return result;
}

console.log(
  solution([
    [3, 5],
    [4, 1],
    [2, 4],
    [5, 10],
  ])
);
