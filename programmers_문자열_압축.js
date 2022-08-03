function solution(s) {
  var answer = "";
  for (var i = 1; i < s.length / 2 + 1; i++) {
    let innerAnswer = "";
    let j = 0;
    console.log(s.substr(j, j + i));
    while (j < s.length) {
      let cnt = 1;
      let X = s.substr(j, i);
      while (s.substr(j, i) === s.substr(j + i, i)) {
        cnt = cnt + 1;
        j = j + i;
      }
      if (cnt > 1) {
        innerAnswer = innerAnswer + cnt.toString();
      }
      innerAnswer = innerAnswer + X;
      j = j + i;
    }
    if (answer === "" || answer.length > innerAnswer.length) {
      answer = innerAnswer;
    }
  }
  if (answer === "") answer = s;
  return answer.length;
}
