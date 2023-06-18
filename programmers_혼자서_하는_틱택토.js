function countBoardState(board) {
  var OCount = 0;
  var XCount = 0;
  var noCount = 0;
  for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      if (board[i][j] === "O") {
        OCount += 1;
      }
      if (board[i][j] === "X") {
        XCount += 1;
      }
      if (board[i][j] === ".") {
        noCount += 1;
      }
    }
  }
  return [OCount, XCount, noCount];
}

function checkWhoIsWinner(board) {
  var isOWinner = 0;
  var isXWinner = 0;
  if (board[0][0] !== ".") {
    const checkPoint = board[0][0];
    if (checkPoint === board[0][1] && checkPoint === board[0][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
    if (checkPoint === board[1][1] && checkPoint === board[2][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
    if (checkPoint === board[1][0] && checkPoint === board[2][0]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
  }

  if (board[0][1] !== ".") {
    const checkPoint = board[0][1];
    if (checkPoint === board[1][1] && checkPoint === board[1][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
  }

  if (board[0][2] !== ".") {
    const checkPoint = board[0][2];
    if (checkPoint === board[1][2] && checkPoint === board[2][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
    if (checkPoint === board[1][1] && checkPoint === board[2][0]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
  }

  if (board[1][0] !== ".") {
    const checkPoint = board[1][0];
    if (checkPoint === board[1][1] && checkPoint === board[1][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
  }

  if (board[2][0] !== ".") {
    const checkPoint = board[2][0];
    if (checkPoint === board[2][1] && checkPoint === board[2][2]) {
      if (checkPoint === "X") isXWinner += 1;
      if (checkPoint === "O") isOWinner += 1;
    }
  }

  return [isOWinner, isXWinner];
}

function solution(board) {
  const [OCount, XCount, noCount] = countBoardState(board);
  const [isOWinner, isXWinner] = checkWhoIsWinner(board);
  console.log(OCount, XCount, noCount, isOWinner, isXWinner);
  if (noCount === 9) return 1;

  if (OCount !== XCount && OCount !== XCount + 1) {
    return 0;
  }

  if (isXWinner > 1) return 0;

  const isOWinnerBoolean = isOWinner !== 0;
  const isXWinnerBoolean = isXWinner !== 0;
  if (isOWinnerBoolean && isXWinnerBoolean) return 0;
  if (isOWinnerBoolean) {
    if (OCount !== XCount + 1) return 0;
  }
  if (isXWinnerBoolean) {
    if (OCount !== XCount) return 0;
  }
  return 1;
}
