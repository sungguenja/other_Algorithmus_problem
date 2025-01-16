function calculateEdgeY(x, r) {
  if (r ** 2 - x ** 2 <= 0) return 0;
  return Math.sqrt(r ** 2 - x ** 2);
}

function solution(r1, r2) {
  var piecePosition = 0;

  for (var i = 1; i < r2; i++) {
    const startY = Math.ceil(calculateEdgeY(i, r1));
    const endY = Math.floor(calculateEdgeY(i, r2));
    startY === 0
      ? (piecePosition += endY - startY)
      : (piecePosition += endY - startY + 1);
  }

  return piecePosition * 4 + (r2 - r1 + 1) * 4;
}
