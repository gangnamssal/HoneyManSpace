// 문자열 my_string이 매개변수로 주어질 때
// 수식을 계산한 값을 return

// 연산자는 +, -만 존재
// 문자열의 시작과 끝에는 공백 x
// 0으로 시작하는 숫자는 없다.
// 잘못된 수식은 없다.
// return 정수형
// 숫자와 연산자는 공백 하나로 구분

function solution(my_string) {
    // 수식을 판별하는 정규 표현식
    const regExp = /[+-]/g;
    // 공백을 기준으로 문자열을 나눈 뒤 숫자만 뽑아 배열로 만든다.
    const strNumArr = my_string.split(' ').filter(item => !regExp.test(item));
    // 수식만 모은 배열
    const strCalArr = my_string.match(regExp);
    // 결과값 (초기값을 숫자 배열의 첫 번째 값으로 설정하여 수식과 수의 갯수를 맞춘다.)
    let result = Number(strNumArr[0]);

    for (let n = 0; n < strCalArr.length; n++) {
        if (strCalArr[n] === '+') {
            result += Number(strNumArr[n+1]);
        } else {
            result -= Number(strNumArr[n+1]);
        }
    }

    return result
}

