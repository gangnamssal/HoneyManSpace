// 대소문자로 이루어진 문자열 매개변수로 주어짐
// 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 뒤 return
function solution(my_string) {
    const result = my_string.toLowerCase().split('').sort().join('')
    return result
}
