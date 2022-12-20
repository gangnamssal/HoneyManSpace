// 문자열 my_string이 매개변수
// 대소문자를 서로 변경하여 return
function solution(my_string) {
    let result = '' // 결과값
    const regExp1 = /[A-Z]/ // 대문자 정규표현식

    for (const word of my_string) {
        // 대문자면 소문자로 변경
        if (regExp1.test(word)) {
            result += word.toLowerCase()
        } else {
            // 소문자면 대문자로 변경
            result += word.toUpperCase()
        }
    }
    return result
}
