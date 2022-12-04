function solution(s) {
  var answer = 0;
  let target = s[0];
  let targetCnt = 0;
  let nonTargetCnt = 0;
  for (i in s) {
    if (targetCnt === nonTargetCnt) {
      answer += 1;
      target = s[i];
    }
    if (s[i] === target) {
      targetCnt += 1;
    } else {
      nonTargetCnt += 1;
    }
  }
  return answer;
}
