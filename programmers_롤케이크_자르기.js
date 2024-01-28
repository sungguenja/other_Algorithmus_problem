function solution(topping) {
  var answer = 0;
  const olderBrother = new Set(topping);
  const elderBrother = new Set();
  const toppingDictionary = new Object();
  topping.map((toppingItem) =>
    toppingDictionary.hasOwnProperty(toppingItem)
      ? (toppingDictionary[toppingItem] += 1)
      : (toppingDictionary[toppingItem] = 1)
  );

  topping.map((toppingItem) => {
    if (toppingDictionary[toppingItem] >= 1) {
      toppingDictionary[toppingItem] -= 1;
    }
    if (toppingDictionary[toppingItem] === 0) {
      olderBrother.delete(toppingItem);
    }
    elderBrother.add(toppingItem);
    if (olderBrother.size === elderBrother.size) {
      answer += 1;
    }
  });

  return answer;
}
