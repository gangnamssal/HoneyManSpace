// 한 마리당 쿠폰 한 장 발급
// 쿠폰 열 장을 모으면 한 마리 서비스
// 서비스 치킨에도 쿠폰이 발급
// 시켜먹은 치킨의 수 chichen이 매개변수
// 최대 서비스 치킨의 수를 return
function solution(chicken) {
  // 치킨의 초기 값은 1081장
  let result = 0;
  let temp = chicken % 10; // 108개를 주문하면 쿠폰은 1개가 남는다.
  let answer = Math.floor(chicken / 10); // 108개의 닭 주문, 108 쿠폰 발급
  result += answer;
  answer += temp;

  while (1) {
    temp = answer % 10;
    answer = Math.floor(answer / 10); // 10
    result += answer;
    if (answer === 0) {
      break;
    }
    answer += temp;
  }

  return result;
}

console.log(solution(1081));
