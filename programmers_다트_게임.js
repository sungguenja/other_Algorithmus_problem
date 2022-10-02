function solution(dartResult) {
  var answer = 0;
  const multipleString = ["S", "D", "T"];
  const rewardString = ["*", "#"];
  var nowNumberString = "";
  var beforeNumber = 0;
  var resetTrigger = false;
  for (let dartString of dartResult) {
    if (multipleString.indexOf(dartString) > -1) {
      resetTrigger = true;
      nowNumberString = Number(nowNumberString);
      if (dartString === "S") nowNumberString = nowNumberString ** 1;
      else if (dartString === "D") nowNumberString = nowNumberString ** 2;
      else if (dartString === "T") nowNumberString = nowNumberString ** 3;
    } else if (rewardString.indexOf(dartString) > -1) {
      resetTrigger = true;
      nowNumberString = Number(nowNumberString);
      if (dartString === "*") {
        nowNumberString = nowNumberString * 2;
        answer += beforeNumber;
        beforeNumber = 0;
      } else if (dartString === "#") nowNumberString = nowNumberString * -1;
    } else {
      if (resetTrigger) {
        beforeNumber = nowNumberString;
        answer += nowNumberString;
        nowNumberString = "";
        resetTrigger = false;
      }
      nowNumberString += dartString;
    }
  }
  answer += nowNumberString;
  return answer;
}
