// 정수 배열 array가 매개변수로 주어질 때,
// 7이 총 몇 개 있는지 return 
function solution(array) {
    let result = 0 // 결과를 저장하는 변수
    array.forEach((item, index, arr) => {
        const strItem = item + '' // 배열의 요소를 문자열로 변경
        const regExp = /7/g // 정규 표현식을 활용해 7을 찾는다.
        const num = strItem.match(regExp) ?? 0 // 7을 찾은 배열
        result += !num ? num : num.length
    })
    return result
}
