/**
 * @param {[1,2,3,4,5,6,7,8,9]} priorities
 * @param {number} location
 * @returns
 */
function solution(priorities, location) {
  var answer = 0;
  var nowFirstWork = Math.max(...priorities);
  var nowLocation = location;
  while (nowLocation >= 0) {
    const nowWork = priorities.shift();
    nowLocation -= 1;
    if (nowWork === nowFirstWork) {
      answer += 1;
      nowFirstWork = Math.max(...priorities);
      if (nowLocation === -1) break;
      continue;
    }
    priorities.push(nowWork);
    if (nowLocation === -1) nowLocation = priorities.length - 1;
  }
  return answer;
}
