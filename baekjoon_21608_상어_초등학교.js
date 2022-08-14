function getBestPosition(nowPosition, afterPoint, clearPositionCount, i, j) {
  if (nowPosition[2] < afterPoint) {
    return [i, j, afterPoint, clearPositionCount];
  } else if (nowPosition[2] > afterPoint) {
    return nowPosition;
  }

  if (nowPosition[3] < clearPositionCount) {
    return [i, j, afterPoint, clearPositionCount];
  } else if (nowPosition[3] > clearPositionCount) {
    return nowPosition;
  }

  if (nowPosition[0] > i) {
    return [i, j, afterPoint, clearPositionCount];
  } else if (nowPosition[0] < i) {
    return nowPosition;
  }

  if (nowPosition[2] > j) {
    return [i, j, afterPoint, clearPositionCount];
  } else {
    return nowPosition;
  }
}

function givePositionInClassRoom(size, roomState, peopleLove) {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  for (var p = 0; p < peopleLove.length; p++) {
    let bestPosition = [-1, -1, -1, -1];
    const lovedPeople = peopleLove[p].slice(1);
    const nowPeople = peopleLove[p][0];
    for (var i = 0; i < size; i++) {
      for (var j = 0; j < size; j++) {
        if (roomState[i][j] !== undefined) {
          continue;
        }
        let positionPoint = 0;
        let clearPosition = 0;
        for (var k = 0; k < 4; k++) {
          const ni = i + di[k];
          const nj = j + dj[k];
          if (0 <= ni && ni < size && 0 <= nj && nj < size) {
            if (roomState[ni][nj] === undefined) {
              clearPosition += 1;
              continue;
            }
            if (lovedPeople.includes(roomState[ni][nj][0])) {
              positionPoint += 1;
            }
          }
        }
        bestPosition = getBestPosition(
          bestPosition,
          positionPoint,
          clearPosition,
          i,
          j
        );
      }
    }
    roomState[bestPosition[0]][bestPosition[1]] = [nowPeople, p];
  }
  return roomState;
}

function getPointWithPosition(nowClassRoom, peopleLove, size) {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  let point = 0;
  for (var i = 0; i < size; i++) {
    for (var j = 0; j < size; j++) {
      const p = nowClassRoom[i][j][1];
      let peopleCnt = 0;
      const lovedPeople = peopleLove[p].slice(1);
      for (var k = 0; k < 4; k++) {
        const ni = i + di[k];
        const nj = j + dj[k];
        if (0 <= ni && ni < size && 0 <= nj && nj < size) {
          if (lovedPeople.includes(nowClassRoom[ni][nj][0])) {
            peopleCnt += 1;
          }
        }
      }
      switch (peopleCnt) {
        case 1:
          point += 1;
          break;
        case 2:
          point += 10;
          break;
        case 3:
          point += 100;
          break;
        case 4:
          point += 1000;
          break;
      }
    }
  }
  return point;
}

const fs = reqiure("fs");
let input = fs.readFileSync("./input.txt").toString();
input = input.trim().split("\n");
for (var i = 0; i < input.length; i++) {
  input[i] = input[i].split(" ");
}

const N = input[0];
const classRoom = new Array(N);
for (var i = 0; i < N; i++) {
  classRoom[i] = new Array(N);
}

const peoplePositionClassRoom = givePositionInClassRoom(
  N,
  classRoom,
  input.slice(1)
);

console.log(getPointWithPosition(peoplePositionClassRoom, input.slice(1), N));
