/**
 *
 * @param {string} targetNumber
 * @param {number} targetBase
 * @returns {number}
 */
function formatNumber(targetNumber, targetBase) {
  var answer = 0;
  var cnt = 0;
  for (var i = targetNumber.length - 1; i > -1; i--) {
    answer += Number(targetNumber[i]) * targetBase ** cnt;
    cnt++;
  }
  return answer;
}
/**
 *
 * @param {string[]} expressions
 * @returns {string[]}
 */
function solution(expressions) {
  const baseFormation = [
    false,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
  ]; // 0 ~ 9
  const XCase = [];
  expressions.forEach((item) => {
    const splitExpression = item.split(" ");
    var maximumNum = -1;
    for (var i = 0; i < splitExpression[0].length; i++) {
      if (Number(splitExpression[0][i]) > maximumNum)
        maximumNum = Number(splitExpression[0][i]);
    }
    for (var i = 0; i < splitExpression[2].length; i++) {
      if (Number(splitExpression[2][i]) > maximumNum)
        maximumNum = Number(splitExpression[2][i]);
    }
    if (splitExpression[4] !== "X") {
      for (var i = 0; i < splitExpression[4].length; i++) {
        if (Number(splitExpression[4][i]) > maximumNum)
          maximumNum = Number(splitExpression[4][i]);
      }
    } else {
      XCase.push(item);
    }
    if (baseFormation[maximumNum]) {
      for (var i = 0; i <= maximumNum; i++) {
        baseFormation[i] = false;
      }
    }

    if (splitExpression[4] === "X") return;

    for (var j = 0; j < 10; j++) {
      if (!baseFormation[j]) continue;

      const AInTen = formatNumber(splitExpression[0], j);
      const BInTen = formatNumber(splitExpression[2], j);
      const CInTen = formatNumber(splitExpression[4], j);
      const isPlus = splitExpression[1] === "+";

      if (isPlus && AInTen + BInTen !== CInTen) baseFormation[j] = false;
      if (!isPlus && AInTen - BInTen !== CInTen) baseFormation[j] = false;
    }
  });

  const isOnly = baseFormation.filter((item) => item).length === 1;
  if (isOnly) {
    const isOnlyAnswer = [];
    const targetBase = baseFormation.findIndex((item) => item);

    XCase.forEach((item) => {
      const splitExpression = item.split(" ");
      const AInTen = formatNumber(splitExpression[0], targetBase);
      const BInTen = formatNumber(splitExpression[2], targetBase);
      const isPlus = splitExpression[1] === "+";
      const CInTen = isPlus ? AInTen + BInTen : AInTen - BInTen;
      isOnlyAnswer.push(
        `${splitExpression[0]} ${isPlus ? "+" : "-"} ${
          splitExpression[2]
        } = ${CInTen.toString(targetBase)}`
      );
    });

    return isOnlyAnswer;
  }
  const answer = [];
  XCase.forEach((item) => {
    const splitExpression = item.split(" ");
    var canCase = null;
    var trigger = true;
    for (var j = 0; j < 10; j++) {
      if (!baseFormation[j]) continue;
      const AInTen = formatNumber(splitExpression[0], j);
      const BInTen = formatNumber(splitExpression[2], j);
      const isPlus = splitExpression[1] === "+";
      const CInTen = isPlus ? AInTen + BInTen : AInTen - BInTen;
      if (canCase === null) canCase = CInTen.toString(j);
      else if (canCase !== CInTen.toString(j)) {
        answer.push(
          `${splitExpression[0]} ${splitExpression[1]} ${splitExpression[2]} = ?`
        );
        trigger = false;
        break;
      }
    }

    if (trigger) {
      answer.push(
        `${splitExpression[0]} ${splitExpression[1]} ${splitExpression[2]} = ${canCase}`
      );
    }
  });
  return answer;
}
