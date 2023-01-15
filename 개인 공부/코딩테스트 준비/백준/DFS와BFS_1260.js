function dfs(start, cnt) {
  if (cnt === parseInt(N) - 1) {
    const result = [...stack];
    dfsResult[dfsResult.length] = result;
    return;
  }
  let found = false;
  for (const i of adjArr[start]) {
    if (dfsResult.length !== 0) {
      return;
    }
    if (visited[i] !== 1) {
      found = true;
      stack[stack.length] = i;
      visited[i] = 1;
      dfs(i, cnt + 1);
      stack.pop();
      visited[i] = null;
    }
  }
  if (!found) {
    const pop = stack.pop();
    visited[pop] = null;
    dfs(pop, cnt - 1);
  }
}

function bfs() {
  while (bfsResult.length !== parseInt(N)) {
    if (queue[0] === undefined) return;
    const front = queue.shift();
    if (visited[front] !== 1) {
      bfsResult[bfsResult.length] = front;
      visited[front] = 1;
      for (const i of adjArr[front]) {
        if (visited[i] !== 1) {
          queue[queue.length] = i;
        }
      }
    }
  }
}

const fs = require("fs");
const input = fs.readFileSync("./example.txt").toString().split("\n");

// N : 정점의 개수, M : 간선의 개수, V : 탐색
const [N, M, V] = input[0].split(" ");

const adjArr = Array.from(Array(parseInt(N) + 1), () => Array());
for (let i = 1; i <= M; i++) {
  const [row, col] = input[i].split(" ");
  adjArr[parseInt(row)] = [...adjArr[parseInt(row)], parseInt(col)];
  adjArr[parseInt(col)] = [...adjArr[parseInt(col)], parseInt(row)];
}

adjArr.map((arr) => {
  return arr.sort((a, b) => a - b);
});

const visited = Array(1000).fill(null);
const stack = [];
visited[parseInt(V)] = 1;
stack[stack.length] = parseInt(V);
const dfsResult = [];

const queue = [parseInt(V)];
const bfsResult = [];

dfs(parseInt(V), 0);
visited[parseInt(V)] = null;

bfs();

console.log(...dfsResult[0]);
console.log(...bfsResult);
