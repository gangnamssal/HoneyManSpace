function helper(arr) {
  const visit = [];
  const result = [];
  let cnt = 0;

  function permutation(cnt) {
    if (cnt === arr.length) {
      visit.push([...result]);
      return;
    }
    for (let i = 0; i < 2; i++) {
      result[cnt] = i;
      permutation(cnt + 1);
    }
  }
  permutation(cnt);
  return visit;
}

const arr = [1, 2, 3];
console.log(helper(arr));
// helper(arr);
