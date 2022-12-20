// 문자열 s가 매개변수로 주어진다.
// s에서 한 번만 등장하는 문자를 사전 순으로
// 정렬한 문자열을 return
function solution(s) {
    const result = [] // 결과값
    const sameStr = [] // 같은 문자를 저장하는 배열
    for (const st of s) {
        // 결과값에 문자열이 존재하지 않으면 추가
        if (result.indexOf(st) === -1 && sameStr.indexOf(st) === -1) {
            result[result.length] = st
        // 같은 문자열이 존재하면 제거하고 같은 문자열을 저장하는 배열에 저장
        } else if(result.indexOf(st) !== -1 && sameStr.indexOf(st) === -1){
            sameStr[sameStr.length] = st
            const idx = result.indexOf(st)
            result.splice(idx,1)
        }
    }
    
    return result.sort().join('')
}
