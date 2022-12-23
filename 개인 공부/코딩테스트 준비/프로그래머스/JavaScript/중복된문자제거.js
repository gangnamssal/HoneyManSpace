// 문자열 my_string이 매개변수
// 중복된 문자를 제거하고 하나의 문자만
// 남긴 문자열을 return

function solution(my_string) {
  // 1. 문자열을 배열로 바꾼다.
  const strArr = my_string.split("");
  // 2. reduce를 이용해 중복을 제거한다.
  const result = strArr.reduce((pre, cur) => {
    // 문자열이 중복되면 추가하지 않는다.
    return pre.indexOf(cur) === -1 ? pre + cur : pre;
  }, "");

  return result;
}
