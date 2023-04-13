// 3의 배수와 숫자 3을 사용하지 않는다.
// 정수 n이 주어질 때 3x 마을에서 사용하는 숫자로 바꿔 return
function solution(n) {
  // 3이 아닌 수를 세는 변수
  let count = 0;
  // 3x 마을의 숫자
  let three = 1;
  // 3이 있는지 확인하는 정규 표현식
  const regExp = /3/;

  while (count !== n) {
    if (regExp.test(three)) {
      three++;
    } else if (!(three % 3)) {
      three++;
    } else {
      count++;
      three++;
    }
  }
  return three - 1;
}

console.log(solution(40));
