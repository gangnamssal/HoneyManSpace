// 문자열 배열 s1, s2의 같은 원소의 개수를 return
function solution(s1, s2) {
    let count = 0

    for (const st of s1) {
        // 한 개의 배열을 순회하여
        // 나머지 한 개의 배열에 요소가 존재하는지 확인
        s2.indexOf(st) !== -1 ? ++count : null 
    }

    return count
}