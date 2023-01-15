function solution(storey) {
  var answer = 0;
  var trigger = false;
  var tenTrigger = 10;
  while (true) {
    if (tenTrigger > storey * 10) break;
    const nowNumber = Math.floor((storey % tenTrigger) / (tenTrigger / 10));
    if (nowNumber < 5) {
      answer += nowNumber;
      trigger = false;
    } else {
      answer += 10 - nowNumber;
      storey += tenTrigger;
      trigger = true;
    }
    console.log(answer, trigger, nowNumber, storey);
    tenTrigger = tenTrigger * 10;
  }
  return answer;
}
