function solution(my_string, n) {
  let res = "";
  for (const a of my_string) {
    for (let i = 0; i < n; i++) {
      res += a;
    }
  }

  return res;
}
