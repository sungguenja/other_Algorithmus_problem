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

/**
 * @param {[number][]} land
 * @param {[number,number]} start
 */
function getOilAndPosition(land, start) {}

/**
 * @param {[number][]} land
 */
function solution(land) {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  const oilPicker = new Array(land[0].length).fill(0);
  const visitLand = new Array(land.length);
  for (var vi = 0; vi < visitLand.length; vi++) {
    visitLand[vi] = new Array(land[0].length).fill(false);
  }
  const N = land.length;
  const M = land[0].length;

  // 기름 확인
  for (var i = 0; i < land.length; i++) {
    for (var j = 0; j < land[0].length; j++) {
      if (visitLand[i][j] || land[i][j] === 0) continue;
      const oilChecker = new Queue();
      oilChecker.enqueue([i, j]);
      visitLand[i][j] = true;
      var oilDrum = 1;
      const oilPosition = [];
      while (!oilChecker.isEmpty()) {
        const [ni, nj] = oilChecker.dequeue();
        visitLand[ni][nj] = true;
        if (!oilPosition.includes(nj)) {
          oilPosition.push(nj);
        }

        for (var k = 0; k < 4; k++) {
          const oi = ni + di[k];
          const oj = nj + dj[k];
          if (
            0 > oi ||
            N <= oi ||
            0 > oj ||
            M <= oj ||
            visitLand[oi][oj] === true ||
            land[oi][oj] === 0
          ) {
            continue;
          }
          visitLand[oi][oj] = true;
          oilChecker.enqueue([oi, oj]);
          oilDrum += 1;
        }
      }
      oilPosition.forEach((pos) => (oilPicker[pos] += oilDrum));
    }
  }

  return Math.max(...oilPicker);
}
