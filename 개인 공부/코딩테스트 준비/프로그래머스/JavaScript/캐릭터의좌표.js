function solution(keyinput, board) {
  const dr = [1, 0, -1, 0];
  const dc = [0, -1, 0, 1];
  let move = 0,
    r = 0,
    c = 0;
  let limitR = Math.floor(board[0] / 2),
    limitC = Math.floor(board[1] / 2);
  for (const a of keyinput) {
    switch (a) {
      case "right":
        move = 0;
        break;
      case "down":
        move = 1;
        break;
      case "left":
        move = 2;
        break;
      case "up":
        move = 3;
        break;
      default:
        break;
    }
    const nr = r + dr[move];
    const nc = c + dc[move];
    if (nr >= -limitR && nc >= -limitC && nr <= limitR && nc <= limitC) {
      r = nr;
      c = nc;
    }
  }
  return [r, c];
}
