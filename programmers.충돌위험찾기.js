/**
 *
 * @param {[number,number][]} arr
 * @param {[number,number]} target
 */
function isInclude(arr, target) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i][0] === target[0] && arr[i][1] === target[1]) return true;
  }
  return false;
}
/**
 *
 * @param {[number,number][]} points
 * @param {number[][]} routes
 * @returns
 */
function solution(points, routes) {
  const center = new Array(101);
  for (var i = 0; i < 101; i++) {
    center[i] = new Array(101);
    for (var j = 0; j < 101; j++) {
      center[i][j] = new Array(0);
    }
  }
  var answer = [];
  for (var i = 0; i < routes.length; i++) {
    var allCount = 0;
    for (var j = 1; j < routes[i].length; j++) {
      const startPoint = routes[i][j - 1];
      const endPoint = routes[i][j];
      var si = points[startPoint - 1][0];
      var sj = points[startPoint - 1][1];
      var ei = points[endPoint - 1][0];
      var ej = points[endPoint - 1][1];
      if (
        allCount === 0 &&
        center[si][sj].includes(allCount) &&
        !isInclude(answer, [si, sj])
      ) {
        answer.push([si, sj]);
      } else {
        center[si][sj].push(allCount);
      }

      while (si !== ei || sj !== ej) {
        if (si !== ei) {
          si > ei ? (si -= 1) : (si += 1);
        } else {
          sj > ej ? (sj -= 1) : (sj += 1);
        }
        allCount++;
        if (center[si][sj].includes(allCount) && !isInclude(answer, [si, sj])) {
          answer.push([si, sj]);
        } else {
          center[si][sj].push(allCount);
        }
      }
    }
  }

  return answer.length;
}
