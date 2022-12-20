// 정수 n이 매개변수
// n의 약수를 오름차순으로 담은 배열을 return
function solution(n) {
    const result = [] // 결과값
    for (let i = 0; i <= n; i++) {
        // n이하의 수를 반복해 약수이면 배열에 넣고 아니면 null을 반환
        n % i === 0 ? result[result.length] = i : null 
    }
    
    return result
}