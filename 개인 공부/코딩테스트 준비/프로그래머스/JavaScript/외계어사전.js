// 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수
// spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가
// dic에 존재하면 1, 아니면 2를 return
function solution(spell, dic) {
  for (let i of dic) {
    let cnt = 0;
    for (let j of spell) {
      if (!i.includes(j)) {
        break;
      }
      cnt++;
    }
    if (cnt === spell.length) {
      return 1;
    }
  }
  return 2;
}

console.log(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]));
