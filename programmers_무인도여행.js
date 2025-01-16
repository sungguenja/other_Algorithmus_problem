class Queue {
  constructor() {
    this._arr = [];
  }
  enqueue(item) {
    this._arr.push(item);
  }
  dequeue() {
    return this._arr.shift();
  }
  isEmpty() {
    return this._arr.length === 0;
  }
}

const di = [0, 1, 0, -1];
const dj = [1, 0, -1, 0];

/**
 * @param {[string][]} maps
 * @returns {[number]}
 */
function solution(maps) {
  const visitMap = new Array(maps.length);
  for (var i = 0; i < maps.length; i++) {
    visitMap[i] = new Array(maps[0].length).fill(false);
  }
  const answer = [];

  for (var i = 0; i < maps.length; i++) {
    for (var j = 0; j < maps[i].length; j++) {
      if (visitMap[i][j] || maps[i][j] === "X") {
        continue;
      }

      var foodCnt = parseInt(maps[i][j]);
      visitMap[i][j] = true;
      const innerQueue = new Queue();
      innerQueue.enqueue([i, j]);
      while (!innerQueue.isEmpty()) {
        const [ni, nj] = innerQueue.dequeue();
        for (var k = 0; k < 4; k++) {
          const oi = ni + di[k];
          const oj = nj + dj[k];
          if (
            oi < 0 ||
            oi >= maps.length ||
            oj < 0 ||
            oj >= maps[0].length ||
            visitMap[oi][oj] ||
            maps[oi][oj] === "X"
          ) {
            continue;
          }
          visitMap[oi][oj] = true;
          foodCnt += parseInt(maps[oi][oj]);
          innerQueue.enqueue([oi, oj]);
        }
      }
      answer.push(foodCnt);
    }
  }
  if (answer.length === 0) return [-1];
  answer.sort((a, b) => a - b);
  return answer;
}
