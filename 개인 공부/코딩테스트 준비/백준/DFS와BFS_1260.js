// 그래프를 DFS로 탐색한 결과
// BFS로 탐색한 결과를 출력하는 프로그램
// 정점이 여러 개인 경우에는 정점 번호가
// 작은 것을 먼저 방문

// 입력 받기
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  input[input.length] = line.split(" ").map((el) => parseInt(el));
});

rl.on("close", () => {
  function DFS(start) {
    const stack = Array(Number.MAX_SAFE_INTEGER); // 스택 배열
    let top = -1; // 현재 배열을 가리키는 변수

    top += 1;
    stack[top] = start; // 첫 번째 스택에 시작점을 넣는다.
    visited[start] = 1;
    // 모든 정점을 방문했는지 확인
    const visitedCnt = visited.reduce((pre, cur) => {
      return pre + cur;
    }, 0);

    while (visitedCnt !== N) {
      for (const i of adjArr[stack[top]]) {
        if (visited[i] === 0) {
          top += 1;
          stack[top] = i;
          visited[i] = 1;
          break;
        }
      }
      top -= 1;
    }
    return stack;
  }

  // 정점의 개수 N, 간선의 개수 M, 정점의 번호 V
  const N = input[0][0];
  const M = input[0][1];
  const V = input[0][2];

  // 간선이 연결하는 두 정점의 번호
  const adjArr = Array.from(Array(N + 1), () => Array());
  // 방문한 곳을 표시하는 배열
  const visited = Array(N + 1);

  for (let i = 1; i <= M; i++) {
    adjArr[input[i][0]].push(input[i][1]);
  }
  console.log(DFS(V));

  process.exit();
});
