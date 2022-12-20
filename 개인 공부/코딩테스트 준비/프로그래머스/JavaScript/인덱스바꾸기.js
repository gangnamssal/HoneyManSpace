// 문자열 my_string, num1, num2가 매개변수
// my_string에서 인덱스 num1과 인덱스 num2에 해당하는
// 문자를 바꾼 문자열을 return 
function solution(my_string, num1, num2) {
    const str1 = my_string[num1] // num1 인덱스의 문자
    const str2 = my_string[num2] // num2 인덱스의 문자
    const strArr = my_string.split('') // 문자열을 배열로 바꾼다.

    strArr.splice(num1,1,str2) // 서로 인덱스 값을 교환한다.
    strArr.splice(num2,1,str1)

    return strArr.join('')
}
