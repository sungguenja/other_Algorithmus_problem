function checkOilList(land) {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  const oliList = [];
  let nowOil = -1;
  const visitLand = new Array(land.length);
  for (var i = 0; i < land.length; i++) {
    visitLand[i] = new Array(land[i].length).fill(false);
  }
  for (var i = 0; i < land.length; i++) {
    for (var j = 0; j < land[i].length; j++) {
      if (visitLand[i][j] === false && land[i][j] === 1) {
        nowOil += 1;
        let oilCnt = 1;
        visitLand[i][j] = nowOil;
        const que = [[i, j]];
        while (que.length > 0) {
          const nowPosition = que.shift();
          for (var k = 0; k < 4; k++) {
            const ni = nowPosition[0] + di[k];
            const nj = nowPosition[1] + dj[k];
            if (ni < 0 || ni >= land.length || nj < 0 || nj >= land[i].length) {
              continue;
            }
            if (visitLand[ni][nj] === false && land[ni][nj] === 1) {
              visitLand[ni][nj] = nowOil;
              que.push([ni, nj]);
              oilCnt += 1;
            }
          }
        }
        oliList.push(oilCnt);
      }
    }
  }
  return [visitLand, oliList];
}

function solution(land) {
  var answer = 0;
  const [oilLand, oliList] = checkOilList(land);
  const visitLand = new Array(land.length);
  for (var i = 0; i < land.length; i++) {
    visitLand[i] = new Array(land[i].length).fill(false);
  }
  for (var j = 0; j < land[0].length; j++) {
    const getOilList = new Array(oliList.length).fill(false);
    let nowAnswer = 0;
    for (var i = 0; i < land.length; i++) {
      const nowPosition = oilLand[i][j];
      if (
        !visitLand[i][j] &&
        nowPosition !== false &&
        !getOilList[nowPosition]
      ) {
        getOilList[nowPosition] = true;
        nowAnswer += oliList[nowPosition];
      }
    }
    if (nowAnswer > answer) {
      answer = nowAnswer;
    }
  }
  return answer;
}
