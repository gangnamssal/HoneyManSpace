// 삼각형의 세 변의 길이가 담긴 배열 sides가 매개변수
// 세 변으로 삼각형을 만들 수 있다면 1, 없다면 2를 return
// 삼각형의 조건 : 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야한다.

function solution(sides) {
    // 1. 배열에서 가장 큰 수를 찾는다.
    const maxV = Math.max(...sides);
    // 2. 배열의 합을 구한다.
    const sumV = sides.reduce((preV, curV) => {
        return preV + curV;
    },0)
    // 3. 두 수의 합을 구한다.
    const otherNumSum = sumV - maxV;

    // 4. 결과를 구한다.
    return maxV >= otherNumSum ? 2 : 1
}