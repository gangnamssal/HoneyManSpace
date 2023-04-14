// 지뢰에 인접한 위, 아래, 좌, 우, 대각선은 모두 위험지역
// 지뢰는 2차원 배열 board에 1로 표시
// 지뢰가 없는 지역은 0으로 표시
// 안전한 지역의 칸 수를 return

function solution(board) {
  const dr = [-1, -1, 0, 1, 1, 1, 0, -1];
  const dc = [0, 1, 1, 1, 0, -1, -1, -1];
  let cnt = Math.pow(board[0].length, 2);

  board.forEach((items, r) => {
    items.forEach((item, c) => {
      if (item === 1) {
        cnt -= 1;
        for (let i = 0; i < 8; i++) {
          let nr = r + dr[i];
          let nc = c + dc[i];

          if (
            nr >= 0 &&
            nc >= 0 &&
            nr < items.length &&
            nc < items.length &&
            board[nr][nc] === 0
          ) {
            board[nr][nc] = 2;
            cnt -= 1;
          }
        }
      }
    });
  });

  return cnt;
}

console.log(
  solution([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
  ])
);
