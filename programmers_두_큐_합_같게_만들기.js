function getAnswer(arr1, arr2, arr1Sum, arr2Sum, cnt, n) {
  if (cnt >= n || arr1.length === 0 || arr2.length === 0) return 9000000;
  if (arr1Sum === arr2Sum) return cnt;
  const arr1Copy = [...arr1];
  const arr2Copy = [...arr2];
  if (arr1Sum > arr2Sum) {
    const arr1Shift = arr1Copy.shift();
    return getAnswer(
      [...arr1Copy],
      [...arr2Copy, arr1Shift],
      arr1Sum - arr1Shift,
      arr2Sum + arr1Shift,
      cnt + 1,
      n
    );
  } else {
    const arr2Shift = arr2Copy.shift();
    return getAnswer(
      [...arr1Copy, arr2Shift],
      [...arr2Copy],
      arr1Sum + arr2Shift,
      arr2Sum - arr2Shift,
      cnt + 1,
      n
    );
  }
}

function solution(queue1, queue2) {
  const queue1Sum = queue1.reduce((acc, item) => acc + item, 0);
  const queue2Sum = queue2.reduce((acc, item) => acc + item, 0);
  var answer = getAnswer(
    queue1,
    queue2,
    queue1Sum,
    queue2Sum,
    0,
    3 * queue1.length
  );
  if (answer === 9000000) return -1;
  return answer;
}
