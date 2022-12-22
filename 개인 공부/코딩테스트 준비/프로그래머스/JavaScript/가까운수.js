// 정수 배열 array, 정수 n이 매개변수
// array에 들어있는 정수 중 n과 가장 가까운 수를 return
function solution(array, n) {
    let result = 0; // 결과값
    let minSub = Number.MAX_SAFE_INTEGER; // 두 수의 차를 저장하는 변수
                                          // 초기값은 큰 수로 정하다.

    // 정수 배열을 순회하면서 n과 현재 수의 차를 구하고 전에
    // 저장되어있던 차보다 작으면 결과값을 바꾼다.
    // 만약 가까운 수가 같다면 더 작은 수를 result에 저장한다.
    array.forEach(item => {
        if (minSub > Math.abs(item - n)) {
            minSub = Math.abs(item - n);
            result = item
        } else if (minSub === Math.abs(item - n) && result > item) {
            result = item
        }
    })

    return result
}
