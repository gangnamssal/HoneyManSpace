// 영어 점수와 수학 점수의 평균으로 등수를 매김
// 영어 점수와 수학 점수를 담은 2차원 정수 배열 score
// 매긴 등수를 담은 배열을 return

function solution(score) {
  const result = []; // 결과값을 저장하는 배열
  // 2차원 배열을 순회하며 평균과 index를 담은 averArr를 만든다.
  const averArr = score.map((scores, index) => {
    return [(scores[0] + scores[1]) / 2, index];
  });
  // 평균을 오름차순으로 정렬
  averArr.sort((a, b) => b[0] - a[0]);

  let currentNum = 0; // 이전 성적을 저장한 변수
  let cnt = 0; // 같은 점수인 학생을 확인하는 변수
  let grade = 0; // 등수

  averArr.forEach((item, index, arr) => {
    // 만약 이전 성적과 같으면 cnt를 1 증가시키고 등수는 바꾸지않고 삽입
    if (currentNum === item[0]) {
      arr[index][2] = grade;
      cnt += 1;
    } else {
      // 만약 이전 성적과 다르면 등수를 1 증가시키고 등수에 cnt를 더하여 삽입
      // 그리고 cnt를 초기화 시켜서 다시 같은 학생의 수를 찾는다.
      grade += 1;
      grade += cnt;
      arr[index][2] = grade;
      cnt = 0;
      currentNum = item[0];
    }
  });
  // 처음 배열의 순서대로 정렬 후 결과 배열에 등수를 넣는다.
  averArr.sort((a, b) => a[1] - b[1]);
  averArr.forEach((item, index) => {
    result[index] = item[2];
  });

  return result;
}
