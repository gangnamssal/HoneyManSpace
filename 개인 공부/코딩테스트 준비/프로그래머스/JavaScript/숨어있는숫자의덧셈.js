// 문자열이 매개변수로 주어진다.
// 문자열은 소문자, 대문자, 자연수로만 구성
// 문자열 안의 자연수들의 합을 return
function solution(myString) {
  // 문자열을 순회하며 숫자를 찾는다.
  let res = 0;
  let num = "";
  const regExp = /[0-9]/;
  for (const a of myString) {
    if (regExp.test(a)) {
      num += a;
    } else {
      res += +num;
      num = "";
    }
  }

  if (num !== "") {
    res += +num;
  }
  return res;
}

solution("aAb1B2cC34oOp");
