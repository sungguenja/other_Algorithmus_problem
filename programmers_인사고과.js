/**
 *
 * @param {[number,number][]} scores
 * @returns {number}
 */
function solution(scores) {
  const wonho = scores[0];
  var answer = 1;
  var MAX_SCORE = 0;

  scores.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]));

  for (var score of scores) {
    if (score[1] < MAX_SCORE) {
      if (score === wonho) return -1;
    } else {
      MAX_SCORE = Math.max(score[1], MAX_SCORE);
      if (score[0] + score[1] > wonho[0] + wonho[1]) answer++;
    }
  }
  return answer;
}
