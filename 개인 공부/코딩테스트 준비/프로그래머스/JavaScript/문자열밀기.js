// 문자열 A를 오른쪽으로 몇 번 밀어서 B가 될 수 있는지 return
// 될 수 없다면 -1을 return

function solution(A, B) {
    const ALength = A.length
    let result = -1
    let currentStr = A.slice()

    if (A===B) {
        return 0
    }

    for (let i = 1; i < ALength; i++) {
        currentStr = currentStr[ALength-1] + currentStr.slice(0,ALength-1)
        if (currentStr === B) {
            result = i
            break
        }
    }
    return result
}

console.log(solution('hello', 'ohell'))