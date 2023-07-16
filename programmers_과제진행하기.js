/**
 * @param {string} hhmm
 * @returns {number}
 */
function makeTimeFromHHMM(hhmm) {
  const [hour, minute] = hhmm.split(":");
  return Number(hour) * 60 + Number(minute);
}

/**
 * @param {[string,string,string][]} plans
 * @returns {string[]}
 */
function solution(plans) {
  const plansWithTime = plans.map((work) => {
    return [work[0], makeTimeFromHHMM(work[1]), Number(work[2])];
  });
  plansWithTime.sort((a, b) => {
    if (a[1] > b[1]) return 1;
    return -1;
  });
  const answer = [];
  const notYet = [];
  const plansCnt = plans.length;
  plansWithTime.forEach((nowWork, index) => {
    if (index === plansCnt - 1) {
      console.log(notYet, "before reverse for");
      answer.push(nowWork[0]);
      for (var i = notYet.length - 1; i >= 0; i--) {
        console.log(notYet[i], i, "in reverse");
        // answer.push(notYet[i][0]);
      }
      console.log(notYet, answer, "before lengthIndex");
      return;
    }
    const futureWork = plansWithTime[index + 1];
    // console.log(futureWork);
    var leftTime = futureWork[1] - nowWork[1];
    if (leftTime >= nowWork[2]) {
      answer.push(nowWork[0]);
      leftTime -= nowWork[2];
      while (leftTime > 0) {
        if (notYet.length === 0) break;
        const notYetLastWork = notYet.pop();
        if (leftTime >= notYetLastWork[2]) {
          answer.push(notYetLastWork[0]);
          leftTime -= notYetLastWork[2];
          continue;
        }
        notYet.push([
          notYetLastWork[0],
          notYetLastWork[1],
          notYetLastWork[2] - leftTime,
        ]);
        leftTime -= notYetLastWork[2];
      }
      console.log(notYet, answer, "leftTime >= nowWork[2]");
      return;
    }
    notYet.push([nowWork[0], nowWork[1], nowWork[2] - leftTime]);
    console.log(notYet, answer, "leftTime >= nowWork[1]");
    return;
  });
  return answer;
}
