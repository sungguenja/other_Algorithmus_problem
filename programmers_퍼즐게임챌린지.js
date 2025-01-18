/**
 *
 * @param {number} nowLevel
 * @param {number} puzzleLevel
 * @param {number} nowConsumed
 * @param {number} prevConsumed
 * @returns {}
 */
function calculateTimeConsumed(
  nowLevel,
  puzzleLevel,
  nowConsumed,
  prevConsumed
) {
  if (nowLevel >= puzzleLevel) return nowConsumed;
  return (prevConsumed + nowConsumed) * (puzzleLevel - nowLevel) + nowConsumed;
}

/**
 *
 * @param {number[]} diffs
 */
function findMax(diffs) {
  var answer = -1;
  diffs.forEach((item) => {
    if (item > answer) answer = item;
  });

  return answer;
}

/**
 *
 * @param {number[]} diffs
 * @param {number[]} times
 * @param {number} limit
 * @returns {number}
 */
function solution(diffs, times, limit) {
  const MAX_LEVEL = findMax(diffs);
  const LENGTH = diffs.length;
  if (LENGTH === 1) return 1;

  var answer = 100001;
  var left = 0;
  var right = MAX_LEVEL + 1;
  var nowAnswer = MAX_LEVEL;
  nowAnswer = Math.ceil(nowAnswer / 2);
  while (left < nowAnswer && nowAnswer < right) {
    var nowTimeConsume = 0;
    for (var i = 0; i < LENGTH; i++) {
      if (i === 0) {
        nowTimeConsume += times[i];
        continue;
      }

      const consumedTime = calculateTimeConsumed(
        nowAnswer,
        diffs[i],
        times[i],
        times[i - 1]
      );
      nowTimeConsume += consumedTime;
    }

    if (nowTimeConsume <= limit) {
      if (nowAnswer < answer) answer = nowAnswer;
      right = nowAnswer;
      nowAnswer = Math.ceil((left + nowAnswer) / 2);
    } else {
      left = nowAnswer;
      nowAnswer = Math.ceil((right + nowAnswer) / 2);
    }
  }
  return answer;
}
