// 두 정수 num과 total이 주어집니다. 
// 연속된 수 num개를 더한 값이 total이 될 때, 
// 정수 배열을 오름차순으로 담아 return
// total이 될 수 없는 테이스 케이스는 없다.

 // 연속된 수를 찾는 함수
//     function zero(num, total) {
//         const divNum = total / num // total을 num으로 나눈 수
//         const result = [divNum] // 결과를 반환하는 Array, 중앙 값을 기준으로 Array를 구한다.
//         const cnt = (num-1) / 2 // 중앙 값에서 몇 번 1을 빼야하는지 counting하는 변수
        
//         for (let i = 0; i < cnt; i++) {
//             result.unshift(result[0] - 1)
//             result.push(result[result.length-1] + 1)
//         }
//         return result
//     }

//     function notZero(num, total) {
//         const divNum = Math.floor(total / num) // total을 num으로 나눈 수의 소수점을 버림
//         const result = [divNum, divNum+1] // 결과를 반환하는 Array, 중앙 값을 기준으로 Array를 구한다.
//         const cnt = (num-2) / 2 // 중앙 값에서 몇 번 1을 빼야하는지 counting하는 변수
//         for (let i = 0; i < cnt; i++) {
//             result.unshift(result[0] - 1)
//             result.push(result[result.length-1] + 1)
//         }
//         return result
//     }


// function FindNum(num, total) {
    
//     return !(total % num) ? zero(num, total) : notZero(num, total)
// }


// // 입력 받기
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// let input = []

// let num = total = 0

// rl.on('line', (line) => {
//     input = line.split(' ').map((item, index, arr) => {
//         return parseInt(item)
//     })
//     num = input[0]
//     total = input[1]

//     rl.close()
// });

// rl.on('close', () => {
//     console.log(FindNum(num,total))
//     process.exit()
// })


function solution(num, total) {
    let result = [];
    if (!(total % num)) {
        const divNum = total / num // total을 num으로 나눈 수
        result = [divNum] // 결과를 반환하는 Array, 중앙 값을 기준으로 Array를 구한다.
        const cnt = (num-1) / 2 // 중앙 값에서 몇 번 1을 빼야하는지 counting하는 변수
        for (let i = 0; i < cnt; i++) {
            result.unshift(result[0] - 1)
            result.push(result[result.length-1] + 1)
        } 
    } else{
        const divNum = Math.floor(total / num) // total을 num으로 나눈 수의 소수점을 버림
        result = [divNum, divNum+1] // 결과를 반환하는 Array, 중앙 값을 기준으로 Array를 구한다.
        const cnt = (num-2) / 2 // 중앙 값에서 몇 번 1을 빼야하는지 counting하는 변수
        for (let i = 0; i < cnt; i++) {
            result.unshift(result[0] - 1)
            result.push(result[result.length-1] + 1)
    }
    }
    
    return result;
}
