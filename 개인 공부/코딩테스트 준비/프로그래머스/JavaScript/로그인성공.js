// 아이디와 패스워드가 담긴 배열 id_pw
// 회원들의 정보가 담긴 2차원 배열 db
// 로그인 성공, 실패에 따른 메시지를 return
// 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 login
// 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 fail
// 비밀번호가 일치하는 회원이 없다면 wrong pw

function solution(id_pw, db) {
  let result = []; // 결과를 저장하는 배열

  // db의 2차원 배열을 순회하면서
  // 아이디와 비밀번호가 일치하면 2, 아이디는 일치하는데 비밀번호가 다르면 1,
  // 나머지는 0을 result 배열에 저장한다.

  for (const item of db) {
    if (id_pw[0] !== item[0] && id_pw[1] !== item[1]) {
      result[result.length] = 0;
    } else if (id_pw[0] !== item[0] && id_pw[1] === item[1]) {
      result[result.length] = 0;
    } else if (id_pw[0] === item[0] && id_pw[1] !== item[1]) {
      result[result.length] = 1;
    } else {
      result[result.length] = 2;
    }
  }

  // 만약 result 배열에 2가 있으면 login, 1이 있으면 wrong pw, 아니면 fail 반환
  return result.indexOf(2) !== -1
    ? "login"
    : result.indexOf(1) !== -1
    ? "wrong pw"
    : "fail";
}
