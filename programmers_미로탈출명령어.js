const di = [1, 0, 0, -1];
const dj = [0, -1, 1, 0];
const dk = ["d", "l", "r", "u"];

/**
 *
 * @param {number} si
 * @param {number} sj
 * @param {number} ei
 * @param {number} ej
 * @param {number} nowCount
 * @param {number} remainCount
 * @returns {boolean}
 */
function canEnd(si, sj, ei, ej, nowCount, remainCount) {
  const minimumMove = Math.abs(ei - si) + Math.abs(ej - sj);
  return (
    minimumMove <= remainCount - nowCount &&
    (remainCount - nowCount - minimumMove) % 2 === 0
  );
}

/**
 *
 * @param {string} targetString
 * @param {string} nowString
 * @returns {boolean}
 */
function whoIsFirst(targetString, nowString) {
  console.log(targetString, nowString, targetString > nowString);
  if (targetString.length > nowString.length) {
    const nowArray = [];
    nowArray.sort();
    return targetString > nowString;
  } else {
    const slicedNow = nowString.slice(0, targetString.length);

    return slicedNow < targetString;
  }
}

/**
 *
 * @param {number} n
 * @param {number} m
 * @param {number} x
 * @param {number} y
 * @param {number} r
 * @param {number} c
 * @param {number} k
 * @param {string} startAnswer
 * @returns
 */
function calculateAnswerFitType(n, m, x, y, r, c, k) {
  const visit = new Array(n + 1);
  for (var i = 0; i < n + 1; i++) {
    const horizon = new Array(m + 1);
    horizon.fill("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz");
    visit[i] = horizon;
  }
  var answer = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz";
  const queue = new Array();
  queue.push([x, y, ""]);
  while (queue.length > 0) {
    const nowPoint = queue.pop();
    if (nowPoint[2].length > k) {
      continue;
    }

    if (nowPoint[0] === r && nowPoint[1] === c && nowPoint[2].length === k) {
      const answerChecker = [answer, nowPoint[2]];
      console.log(answer, nowPoint[2], answer > nowPoint[2]);
      answerChecker.sort();
      answer = answerChecker[0];
      continue;
    }

    for (var d = 0; d < 4; d++) {
      const ni = nowPoint[0] + di[d];
      const nj = nowPoint[1] + dj[d];
      if (ni <= 0 || ni > n || nj <= 0 || nj > m) {
        continue;
      }
      const nk = nowPoint[2] + dk[d];
      const nowVisitString = visit[ni][nj];
      //   console.log(
      //     ni,
      //     nj,
      //     nk,
      //     nk.length > k,
      //     nk === nowVisitString,
      //     !whoIsFirst(nowVisitString, nk),
      //     !canEnd(ni, nj, r, c, nk.length, k),
      //     stringVisit[ni][nj].includes(nk)
      //   );

      if (
        nk.length > k ||
        nk === nowVisitString ||
        !whoIsFirst(nowVisitString, nk) ||
        !canEnd(ni, nj, r, c, nk.length, k)
      ) {
        continue;
      }
      visit[ni][nj] = nk;
      queue.push([ni, nj, nk]);
    }
  }

  return answer;
}
/**
 *
 * @param {number} n
 * @param {number} m
 * @param {number} x
 * @param {number} y
 * @param {number} r
 * @param {number} c
 * @param {number} k
 * @returns {string}
 */
function solution(n, m, x, y, r, c, k) {
  const minimumMove = Math.abs(x - r) + Math.abs(y - c);
  console.log(minimumMove, k, minimumMove - k, (minimumMove - k) % 2 === 1);
  if (minimumMove > k) return "impossible";
  if (minimumMove < k && (k - minimumMove) % 2 === 1) return "impossible";

  return calculateAnswerFitType(n, m, x, y, r, c, k);
}
