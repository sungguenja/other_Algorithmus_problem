function solution(board) {
  const solutionMaximum = board.length * board[0].length * 2;
  const Que = [];
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  var answer = solutionMaximum;
  const visitBoard = new Array(board.length);
  for (var i = 0; i < board.length; i++) {
    visitBoard[i] = [];
    for (var j = 0; j < board[i].length; j++) {
      visitBoard[i].push(solutionMaximum);
      if (board[i][j] === "R") {
        Que.push([i, j, 0]);
        visitBoard[i][j] = 0;
      }
    }
  }

  while (Que.length > 0) {
    const [ii, jj, cnt] = Que.shift();
    if (board[ii][jj] === "G") {
      if (answer > cnt) {
        answer = cnt;
      }
      continue;
    }

    for (var k = 0; k < 4; k++) {
      var ni = ii;
      var nj = jj;
      while (
        ni >= 0 &&
        ni < board.length &&
        nj >= 0 &&
        nj < board[0].length &&
        board[ni][nj] !== "D"
      ) {
        ni += di[k];
        nj += dj[k];
      }
      ni -= di[k];
      nj -= dj[k];
      if (visitBoard[ni][nj] > cnt + 1) {
        visitBoard[ni][nj] = cnt + 1;
        Que.push([ni, nj, cnt + 1]);
      }
    }
  }

  if (answer === solutionMaximum) answer = -1;
  return answer;
}
