function solution(n) {
  const set = new Set();
  const obj = {};

  // n보다 작을 때까지 반복문을 순회
  for (let i = 2; i <= n; i++) {
    // 나누어 떨어지는 수를 저장
    if (n % i === 0 && !obj[i]) {
      set.add(i);
      let num;
      let cnt = 1;
      // 나누어 떨어지는 수의 배수를 저장 => n보다 작을 때까지
      while ((num = ++cnt * i) <= n) {
        if (!obj[num]) {
          obj[num] = true;
        }
      }
    }
  }

  // 결과를 return
  return [...set];
}
