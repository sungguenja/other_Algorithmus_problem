function bfs(maps, N, M) {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  const visit = new Array(M);
  for (var i = 0; i < M; i++) {
    visit[i] = new Array(N);
  }
  visit[0][0] = 0;
  let result = -1;
  const Queue = new Array();
  Queue.push([0, 0, 1]);
  while (Queue.length > 0) {
    const [i, j, cnt] = Queue.shift();
    for (var k = 0; k < 4; k++) {
      const ni = i + di[k];
      const nj = j + dj[k];
      if (0 <= ni && ni < M && 0 <= nj && nj < N) {
        if (
          maps[ni][nj] === 1 &&
          (visit[ni][nj] === undefined || visit[ni][nj] > cnt + 1)
        ) {
          visit[ni][nj] = cnt + 1;
          Queue.push([ni, nj, cnt + 1]);
          if (
            ni === M - 1 &&
            nj === N - 1 &&
            (result === -1 || result > cnt + 1)
          ) {
            result = cnt + 1;
          }
        }
      }
    }
  }
  return result;
}

function solution(maps) {
  const M = maps.length;
  const N = maps[0].length;
  var answer = bfs(maps, N, M);
  return answer;
}
