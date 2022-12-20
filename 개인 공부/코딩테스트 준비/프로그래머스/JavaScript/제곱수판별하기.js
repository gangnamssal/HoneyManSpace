// 정수 n이 제곱수라면 1을 반환
// 아니면 2를 반환

function solution(n) {
    const number = Math.sqrt(n)
    return number - Math.floor(number) === 0 ? 1 : 2
}
