function solution(n, wires) {
  var answer = n * wires.length;
  const visit = new Array(n + 1);
  const routes = new Object();

  for (let wire of wires) {
    if (routes[wire[0]] === undefined) routes[wire[0]] = [];
    if (routes[wire[1]] === undefined) routes[wire[1]] = [];
    routes[wire[0]].push(wire[1]);
    routes[wire[1]].push(wire[0]);
  }

  function BFS(leftStart, rightStart) {
    const Queue = [];
    let leftCnt = -1;
    let rightCnt = -1;
    const leftString = "left";
    const rightString = "right";
    visit[leftStart] = leftString;
    visit[rightStart] = rightString;
    Queue.push([leftStart, leftString]);
    Queue.push([rightStart, rightString]);
    while (Queue.length > 0) {
      const [startPoint, direction] = Queue.shift();

      for (let goal of routes[startPoint]) {
        if (
          (startPoint === leftStart && goal === rightStart) ||
          (startPoint === rightStart && goal === leftStart)
        )
          continue;
        if (visit[goal] === undefined) {
          visit[goal] = direction;
          Queue.push([goal, direction]);
        } else if (visit[goal] !== direction) return false;
      }
    }
    return true;
  }

  for (let wire of wires) {
    for (let i = 0; i < n + 1; i++) {
      visit[i] = undefined;
    }
    const trigger = BFS(wire[0], wire[1]);
    if (!trigger) continue;
    const noneTrigger = false;
    let leftCnt = 0;
    let rightCnt = 0;
    for (let i = 1; i < n + 1; i++) {
      if (visit[i] === undefined) {
        noneTrigger = true;
        break;
      }
      if (visit[i] === "left") leftCnt += 1;
      if (visit[i] === "right") rightCnt += 1;
    }
    if (noneTrigger) continue;
    if (answer > Math.abs(leftCnt - rightCnt))
      answer = Math.abs(leftCnt - rightCnt);
  }
  return answer;
}
