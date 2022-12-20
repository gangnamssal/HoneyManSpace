// my_str을 길이 n씩 잘라서 저장한 배열을 return

function solution(my_str, n) {
    const result = [] // 자른 배열을 저장하는 변수
    const strLength = my_str.length // 문자열 길이
    const count = Math.ceil(strLength / n)  // 몇 번 잘라야 하는지 나타내는 변수
    for (let i = 0; i < count; i++) {
        // 남은 길이가 잘라야하는 길이보다 짧으면 전부 다 자름
        if (strLength-i*n < n) {
            result[i] = my_str.slice(i*n, strLength)
        }
        // 아니라면 n만큼 자름
        result[i] = my_str.slice(i*n,i*n+n)
    }
    return result
}
