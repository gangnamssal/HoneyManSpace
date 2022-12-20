// 정수 배열 array가 매개변수
// 가장 큰 수와 그 수의 인덱스를 담은 배열을 return
function solution(array) {
    // 배열의 요소 중 최댓값을 구함
    const maxNum = Math.max(...array)
    // 구한 최댓값으로 인덱스 값을 구함
    const maxIdx = array.indexOf(maxNum)
    return [maxNum, maxIdx]
}