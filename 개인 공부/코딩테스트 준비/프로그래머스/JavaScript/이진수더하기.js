// 이진수를 의미하는 두 개의 문자열 bin1, bin2가 매개변수
// 두 이진수의 합을 return

function solution(bin1, bin2) {
  // 이진수를 숫자로 변환한 뒤
  // 더하고 결과값을 다시 2진수로 변경
  const bin1Num = parseInt(bin1, 2);
  const bin2Num = parseInt(bin2, 2);

  return (bin1Num + bin2Num).toString(2);
}
