/**
 *
 * @param {number[][]} rc
 * @param {ShiftRow[]} operations
 * @returns {number[][]}
 */
function solution(rc, operations) {
  const N = rc.length;
  const M = rc[0].length;
  var i = 0;
  while (i < operations.length) {
    const oper = operations[i];
    if (oper === "ShiftRow") {
      const operSlice = operations.slice(i, i + N);
      if (operSlice.length === "N" && !operSlice.includes("Rotate")) {
        i += N;
        continue;
      }
      rc.unshift(rc.pop());
      i++;
    } else {
      //   const rightUpper = rc[0].pop();
      //   rc[0].unshift(rc[1][0]);
      //   const leftDowner = rc[N - 1].shift();
      //   rc[N - 1].push(rc[N - 2][M - 1]);
      //   for (var j = 1; j < N - 1; j++) {
      //     rc[j][0] = rc[j + 1][0];
      //     rc[N - j][M - 1] = rc[N - 1 - j][M - 1];
      //   }
      //   rc[1][M - 1] = rightUpper;
      //   rc[N - 2][0] = leftDowner;
      var j = 0;
      while (i + j < operations.length && operations[i + j] === "Rotate") {
        j++;
      }
      const edgeList = [...rc[0]];
      for (var k = 1; k < N - 1; k++) {
        edgeList.push(rc[k][M - 1]);
      }
      const tmpDownEdge = [...rc[N - 1]];
      tmpDownEdge.reverse();
      const tmpLeftEdge = [];
      for (var k = N - 2; k > 0; k--) {
        tmpLeftEdge.push(rc[k][0]);
      }
      const resultEdgeList = [...edgeList, ...tmpDownEdge, ...tmpLeftEdge];
      var rightTrigger = false;
      var downTrigger = false;
      var leftTrigger = false;
      var startRotate = resultEdgeList.length - j;
      var startI = 0;
      var startJ = 0;
      for (var k = 0; k < resultEdgeList.length; k++) {
        rc[startI][startJ] = resultEdgeList[startRotate];
        startRotate++;
        if (startRotate === resultEdgeList.length) {
          startRotate = 0;
        }
        if (!rightTrigger && !downTrigger && !leftTrigger) {
          startJ += 1;
          if (startJ === M - 1) {
            rightTrigger = true;
          }
          continue;
        }
        if (!downTrigger && !leftTrigger) {
          startI += 1;
          if (startI === N - 1) {
            downTrigger = true;
          }
          continue;
        }
        if (!leftTrigger) {
          startJ -= 1;
          if (startJ === 0) {
            leftTrigger = true;
          }
          continue;
        }
        startI -= 1;
      }
      i += j;
    }
  }
  return rc;
}
