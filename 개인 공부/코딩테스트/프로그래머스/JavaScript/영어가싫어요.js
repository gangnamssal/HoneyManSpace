// 영어로 표기되어있는 숫자를 수로 바꾼다.
// 문자열 numbers가 매개변수
// numbers를 정수로 바꿔 return
function solution(numbers) {
    let result = '' // 결과값

    // 숫자를 판단할 Object
    const number = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    // 인수를 순회하면서 object에 포함되는지 체크
    // 포함되면 결과값에 추가
    let st = ''
    for (const word of numbers) {
        st += word
        if (number[st] !== undefined) {
            result += number[st]
            st = ''
        }
    }
    return +result //결과값을 숫자로 바꿔서 return
}
