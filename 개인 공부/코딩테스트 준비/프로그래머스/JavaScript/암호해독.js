// 문자열 cipher와 정수 code가 매개변수
// cipher에서 code의 배수 번째 글자만 진짜 암호
// 해독된 암호 문자열을 return

function solution(cipher, code) {
    let result = '' // 결과값
    // cipher에서 code의 배수 번째 글자를 찾아 result에 더한다.
    for (let i = 0; i < cipher.length; i++) {
        // i+1이 code의 배수인지 확인
        (i+1) % code === 0 ? result += cipher[i] : null
    }

    return result
}