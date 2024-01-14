function solution(numbers, target) {
  var answer = 0;
  const stack = [];
  stack.push([0, 0]);

  while (stack.length) {
    const [nowSum, idx] = stack.pop();
    if (idx === numbers.length) {
      if (nowSum === target) answer++;
      continue;
    }
    for (var k = 0; k < 2; k++) {
      stack.push([
        k === 0 ? nowSum + numbers[idx] : nowSum - numbers[idx],
        idx + 1,
      ]);
    }
  }
  return answer;
}
