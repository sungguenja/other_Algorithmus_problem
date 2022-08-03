function solution(n, computers) {
  var answer = 0;
  const visitStatus = new Array(n);
  for (var i = 0; i < n; i++) {
    if (visitStatus[i] !== undefined) continue;
    const innerVisit = new Array(n);
    innerVisit[i] = true;
    const stack = [i];
    while (stack.length > 0) {
      let node = stack.pop();
      for (var j = 0; j < n; j++) {
        if (computers[node][j] === 0) continue;
        if (innerVisit[j] !== undefined) continue;
        visitStatus[j] = true;
        innerVisit[j] = true;
        stack.push(j);
      }
    }
    answer = answer + 1;
  }
  return answer;
}
