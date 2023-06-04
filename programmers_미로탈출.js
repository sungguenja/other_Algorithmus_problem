function makeVisitArray(N, M) {
  const beforeLever = new Array(N);
  const afterLever = new Array(N);
  for (var i = 0; i < N; i++) {
    beforeLever[i] = new Array(M);
    afterLever[i] = new Array(M);
  }
  return [beforeLever, afterLever];
}

function findStartLeverEnd(maps, N, M) {
  const start = [-1, -1];
  const lever = [-1, -1];
  const end = [-1, -1];
  for (var i = 0; i < N; i++) {
    for (var j = 0; j < M; j++) {
      if (maps[i][j] === "S") {
        start[0] = i;
        start[1] = j;
      }
      if (maps[i][j] === "L") {
        lever[0] = i;
        lever[1] = j;
      }
      if (maps[i][j] === "E") {
        end[0] = i;
        end[1] = j;
      }
    }
  }
  return [start, lever, end];
}

function solution(maps) {
  var answer = -1;
  const di = [-1, 0, 1, 0];
  const dj = [0, 1, 0, -1];
  const N = maps.length;
  const M = maps[0].length;
  const [beforeLever, afterLever] = makeVisitArray(N, M);
  const [start, lever, end] = findStartLeverEnd(maps, N, M);

  const que = new Array();
  que.push([start[0], start[1], 0, false]);

  while (que.length > 0) {
    const [i, j, cnt, isLeverOn] = que.shift();
    if (isLeverOn && i == end[0] && j == end[1]) {
      if (answer == -1 || answer > cnt) {
        answer = cnt;
      }
      continue;
    }

    for (var k = 0; k < 4; k++) {
      const ni = i + di[k];
      const nj = j + dj[k];
      if (0 <= ni && ni < N && 0 <= nj && nj < M && maps[ni][nj] !== "X") {
        const nCnt = cnt + 1;
        if (
          !isLeverOn &&
          (beforeLever[ni][nj] == undefined || beforeLever[ni][nj] > nCnt)
        ) {
          beforeLever[ni][nj] = nCnt;
          if (maps[ni][nj] == "L") {
            que.push([ni, nj, nCnt, true]);
          } else {
            que.push([ni, nj, nCnt, isLeverOn]);
          }
        }

        if (
          isLeverOn &&
          (afterLever[ni][nj] == undefined || afterLever[ni][nj] > nCnt)
        ) {
          afterLever[ni][nj] = nCnt;
          que.push([ni, nj, nCnt, isLeverOn]);
        }
      }
    }
  }
  return answer;
}
