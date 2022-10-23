function solution(n) {
  const threeNumber = n.toString(3);
  const reverseThreeNumber = threeNumber.split("");
  var answer = reverseThreeNumber.reduce(
    (previousValue, nowValue, index) =>
      previousValue + Number(nowValue) * 3 ** index,
    0
  );
  return answer;
}
