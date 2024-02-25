function solution(edges) {
  let startNode = 0;
  let normalDonutGraph = 0;
  let barGraph = 0;
  let extendDonutGraph = 0;
  const graphMap = {};
  for (var [start, goal] of edges) {
    if (!graphMap[start]) {
      graphMap[start] = {
        insert: [],
        extract: [goal],
        nodeNumber: start,
      };
    } else {
      graphMap[start].extract.push(goal);
    }

    if (!graphMap[goal]) {
      graphMap[goal] = {
        insert: [start],
        extract: [],
        nodeNumber: goal,
      };
    } else {
      graphMap[goal].insert.push(start);
    }

    if (
      graphMap[start].insert.length === 0 &&
      graphMap[start].extract.length >= 2
    )
      startNode = start;
    if (
      graphMap[goal].insert.length === 0 &&
      graphMap[goal].extract.length >= 2
    )
      startNode = goal;
  }

  const startNodeNumber = Number(startNode);
  for (const [key, value] of Object.entries(graphMap)) {
    if (value.extract.length === 0) barGraph += 1;
    if (value.extract.length === 2 && value.insert.length >= 2)
      extendDonutGraph += 1;
  }
  normalDonutGraph =
    graphMap[startNode].extract.length - barGraph - extendDonutGraph;

  return [startNodeNumber, normalDonutGraph, barGraph, extendDonutGraph];
}
