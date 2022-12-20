// 정수 num, k가 매개변수
// num을 이루는 숫자 중에 k가 있으면
// 숫자가 있는 자리 수를 return
// 없으면 -1

function solution(num, k) {
    // 정수를 문자열로 변경
    const numStr = num + ''
    // 같은 숫자가 존재하면 인덱스 값에 +1, 없으면 -1을 return
    return numStr.indexOf(k) !== -1 ? numStr.indexOf(k) + 1 : -1
}