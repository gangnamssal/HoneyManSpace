// 369게임에서 머쓱이가 말해야하는 숫자 order가 매개변수
// 쳐야할 박수 횟수를 return

function solution(order) {
    // 숫자값 order를 문자열로 변경한 뒤 정규 표현식으로 3,6,9가
    // 들어가는 배열을 반환한 뒤 길이를 구한다.
    const regExp = /[369]/g     // 3,6,9 정규 표현식
    const result = ('' + order).match(regExp)   // 3,6,9가 포함된 배열

    return result === null ? 0 : result.length  // 배열이 null이면 0 아니면 길이를 반환
}
