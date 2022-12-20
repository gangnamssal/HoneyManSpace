// 수식들이 들어있는 문자열 배열 quiz가 주어진다.
// 수식이 옳다면 O, 틀리다면 X를 return
function solution(quiz) {
    const result = []

    // 배열을 순회
    quiz.forEach( item => {
        let number = null         // 숫자를 저장하는 변수
        let notNumber = null      // 연산자를 저장하는 변수
        let calNum = 0          // 현재까지 계산된 결과

        const itemArr = item.split(' ')  // 띄어쓰기 기준으로 문자열을 나눈다.

        itemArr.forEach( el => {
            if (!Number.isInteger(+el)) {
                // 연산자면 실행
                notNumber = el
            } else if (Number.isInteger(+el) && el !== '=') {
                // 수면 실행
                if (number !== null && notNumber !== null && notNumber === '-') {
                    // 연산자랑 수가 있고 수가 또 나오면 -를 계산
                    calNum += number - (+el)
                    number = null
                    notNumber = null
                } else if (number !== null && notNumber !== null && notNumber === '+') {
                    // 연산자랑 수가 있고 수가 또 나오면 +를 계산
                    calNum += number + (+el)
                    number = null
                    notNumber = null
                } else {
                    // 수가 없는 상태면 수를 저장
                    number = +el
                }
            }
        })
        // 비교하는 과정
        result[result.length] = calNum === (number ?? +notNumber) ? 'O' : 'X'
    })
    return result
}
