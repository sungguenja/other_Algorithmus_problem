function yBankShot(x1, y1, x2, y2) {
  return parseInt(
    ((x1 ** 2 + x2 ** 2 + 2 * x1 * x2) *
      (x1 ** 2 + (y1 - (x2 * y1 + x1 * y2) / (x1 + x2)) ** 2)) /
      x1 ** 2
  );
}

function xBankShot(x1, y1, x2, y2) {
  return parseInt(
    ((y1 ** 2 + y2 ** 2 + 2 * y1 * y2) *
      (y1 ** 2 + ((x2 * y1 + x1 * y2) / (y1 + y2) - x1) ** 2)) /
      y1 ** 2
  );
}

function upBankShot(x1, y1, x2, y2, n) {
  return parseInt(
    ((2 * n - y2 - y1) ** 2 / Math.abs(n - y1) ** 2) *
      ((n - y1) ** 2 +
        ((Math.abs(n - y1) * x2 + Math.abs(n - y2) * x1) / (2 * n - y1 - y2) -
          x1) **
          2)
  );
}

function rightBankShot(x1, y1, x2, y2, m) {
  return parseInt(
    ((2 * m - x1 - x2) ** 2 / Math.abs(m - x1) ** 2) *
      ((m - x1) ** 2 +
        (y1 -
          (Math.abs(m - x2) * y1 + Math.abs(m - x1) * y2) /
            (2 * m - x1 - x2)) **
          2)
  );
}

// 구석케이스를 생각안함 (귀찮아서 안할래)
function solution(m, n, startX, startY, balls) {
  var answer = [];
  for (ball of balls) {
    const lengthList = [];
    if (startY !== ball[1] || ball[0] >= startX) {
      lengthList.push(yBankShot(startX, startY, ball[0], ball[1]));
    }
    if (startX !== ball[0] || ball[1] >= startY) {
      lengthList.push(xBankShot(startX, startY, ball[0], ball[1]));
    }
    if (startY !== ball[1] || ball[0] <= startX) {
      lengthList.push(rightBankShot(startX, startY, ball[0], ball[1], m));
    }
    if (startX !== ball[0] || ball[1] <= startY) {
      lengthList.push(upBankShot(startX, startY, ball[0], ball[1], n));
    }
    answer.push(Math.min(...lengthList));
  }
  return answer;
}
