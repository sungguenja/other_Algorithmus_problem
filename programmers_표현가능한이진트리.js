/**
 *
 * @param {string} decimalString
 */
function checkZeroNode(decimalString) {
  if (decimalString.length === 3) return decimalString === "000";
  const headDecimal = decimalString.slice(
    0,
    Math.floor(decimalString.length / 2)
  );
  const tailDecimal = decimalString.slice(
    Math.floor(decimalString.length / 2) + 1,
    decimalString.length
  );

  return checkZeroNode(headDecimal) && checkZeroNode(tailDecimal);
}
/**
 *
 * @param {string} decimalString
 */
function checkCanDecimal(decimalString) {
  if (decimalString.length === 3)
    return decimalString[1] === "1" || decimalString === "000";

  const headDecimal = decimalString.slice(
    0,
    Math.floor(decimalString.length / 2)
  );
  const middleDecimal = decimalString[Math.floor(decimalString.length / 2)];
  const tailDecimal = decimalString.slice(
    Math.floor(decimalString.length / 2) + 1,
    decimalString.length
  );
  if (middleDecimal === "0")
    return checkZeroNode(headDecimal) && checkZeroNode(tailDecimal);

  return checkCanDecimal(headDecimal) && checkCanDecimal(tailDecimal);
}

const CAN_DECIMAL_LENGTH = [1, 3, 7, 15, 31, 63];

/**
 *
 * @param {number[]} numbers
 * @returns {number[]}
 */
function solution(numbers) {
  const decimalNumbers = numbers.map((item) => {
    if (item === 1) return "111";
    var decimalItem = item.toString(2);
    while (!CAN_DECIMAL_LENGTH.includes(decimalItem.length)) {
      decimalItem = "0" + decimalItem;
    }

    return decimalItem;
  });
  const answer = decimalNumbers.map((item) => (checkCanDecimal(item) ? 1 : 0));
  return answer;
}
