const INF = Infinity;

function yBankShot(x1, y1, x2, y2, m, n) {
  const a = (x2 * y1 + x1 * y2) / (x1 + x2);

  if (a === 0 && y1 / x1 === y2 / x2 && x1 > x2 && y1 > y2) {
    return INF;
  }

  if (a === n && (y1 - n) / x1 === (y2 - n) / x2 && x1 > x2 && y1 < y2) {
    return INF;
  }

  if (a === y1 || a === y2) {
    if (x2 < x1) {
      return INF;
    }
  }

  return parseInt(
    ((x1 ** 2 + x2 ** 2 + 2 * x1 * x2) *
      (x1 ** 2 + (y1 - (x2 * y1 + x1 * y2) / (x1 + x2)) ** 2)) /
      x1 ** 2
  );
}

function xBankShot(x1, y1, x2, y2, m, n) {
  const b = (y1 * x2 + y2 * x1) / (y1 + y2);

  if (b === 0 && y1 / x1 === y2 / x2 && x1 > x2 && y1 > y2) {
    return INF;
  }

  if (b === m && y1 / (x1 - m) === y2 / (x2 - m) && x1 < x2 && y1 > y2) {
    return INF;
  }

  if (b === x1 || b === x2) {
    if (y1 > y2) {
      return INF;
    }
  }

  return parseInt(
    ((y1 ** 2 + y2 ** 2 + 2 * y1 * y2) *
      (y1 ** 2 + ((x2 * y1 + x1 * y2) / (y1 + y2) - x1) ** 2)) /
      y1 ** 2
  );
}

function upBankShot(x1, y1, x2, y2, m, n) {
  const b = ((n - y1) * x2 + (n - y2) * x1) / (2 * n - y1 - y2);

  if (b === 0 && (y1 - n) / x1 === (y2 - n) / x2 && x1 > x2 && y1 < y2) {
    return INF;
  }

  if (
    b === m &&
    (y1 - n) / (x1 - m) === (y2 - n) / (x2 - m) &&
    x1 < x2 &&
    y1 < y2
  ) {
    return INF;
  }

  if (b === x1 || b === x2) {
    if (y1 < y2) {
      return INF;
    }
  }

  return parseInt(
    ((2 * n - y2 - y1) ** 2 / Math.abs(n - y1) ** 2) *
      ((n - y1) ** 2 +
        ((Math.abs(n - y1) * x2 + Math.abs(n - y2) * x1) / (2 * n - y1 - y2) -
          x1) **
          2)
  );
}

function rightBankShot(x1, y1, x2, y2, m, n) {
  const a = ((m - x2) * y1 + (m - x1) * y2) / (2 * m - x1 - x2);

  if (a === 0 && y1 / (x1 - m) === y2 / (x2 - m) && x1 < x2 && y1 > y2) {
    return INF;
  }

  if (
    a === n &&
    (y1 - n) / (x1 - m) === (y2 - n) / (x2 - m) &&
    x1 < x2 &&
    y1 < y2
  ) {
    return INF;
  }

  if (a === y1 || a === y2) {
    if (x2 > x1) {
      return INF;
    }
  }

  return parseInt(
    ((2 * m - x1 - x2) ** 2 / Math.abs(m - x1) ** 2) *
      ((m - x1) ** 2 +
        (y1 -
          (Math.abs(m - x2) * y1 + Math.abs(m - x1) * y2) /
            (2 * m - x1 - x2)) **
          2)
  );
}

function solution(m, n, startX, startY, balls) {
  var answer = [];
  for (ball of balls) {
    const lengthList = [];
    lengthList.push(yBankShot(startX, startY, ball[0], ball[1], m, n));
    lengthList.push(xBankShot(startX, startY, ball[0], ball[1], m, n));
    lengthList.push(rightBankShot(startX, startY, ball[0], ball[1], m, n));
    lengthList.push(upBankShot(startX, startY, ball[0], ball[1], m, n));
    answer.push(Math.min(...lengthList));
  }
  return answer;
}
