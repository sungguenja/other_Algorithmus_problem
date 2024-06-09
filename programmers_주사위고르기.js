const getCombination = (arr, n) => {
  if (n === 1) return arr.map((el) => [el]);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combis = getCombination(rest, n - 1);
    const attached = combis.map((combi) => [fixed, ...combi]);
    result.push(...attached);
  });

  return result;
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @returns {[number, number]}
 */
const getOneDiceWinCnt = (aDice, bDice) => {
  const sortedADice = aDice.sort((a, b) => a - b);
  const sortedBDice = bDice.sort((a, b) => a - b);
  const caseLength = aDice.length;
  let aWinCnt = 0;
  let bWinCnt = 0;
  for (var i = 0; i < caseLength; i++) {
    if (sortedADice[i] > sortedBDice[caseLength - 1]) {
      aWinCnt += caseLength * (caseLength - i);
      break;
    }
    for (var j = 0; j < caseLength; j++) {
      if (sortedADice[i] > sortedBDice[j]) aWinCnt++;
      if (sortedADice[i] < sortedBDice[j]) bWinCnt++;
    }
  }
  if (aWinCnt >= bWinCnt) return [aWinCnt, 0];
  else return [bWinCnt, 1];
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @returns {[number, number]}
 */
const getTwoDiceWinCnt = (aDice, bDice) => {
  const aSumCase = [];
  const bSumCase = [];
  for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
      aSumCase.push(aDice[0][i] + aDice[1][j]);
      bSumCase.push(bDice[0][i] + bDice[1][j]);
    }
  }
  return getOneDiceWinCnt(aSumCase, bSumCase);
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @returns {[number, number]}
 */
const getThreeDiceWinCnt = (aDice, bDice) => {
  const aSumCase = [];
  const bSumCase = [];
  for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
      for (var k = 0; k < 6; k++) {
        aSumCase.push(aDice[0][i] + aDice[1][j] + aDice[2][k]);
        bSumCase.push(bDice[0][i] + bDice[1][j] + bDice[2][k]);
      }
    }
  }
  return getOneDiceWinCnt(aSumCase, bSumCase);
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @returns {[number, number]}
 */
const getFourDiceWinCnt = (aDice, bDice) => {
  const aSumCase = [];
  const bSumCase = [];
  for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
      for (var k = 0; k < 6; k++) {
        for (var l = 0; l < 6; l++) {
          aSumCase.push(aDice[0][i] + aDice[1][j] + aDice[2][k] + aDice[3][l]);
          bSumCase.push(bDice[0][i] + bDice[1][j] + bDice[2][k] + bDice[3][l]);
        }
      }
    }
  }
  return getOneDiceWinCnt(aSumCase, bSumCase);
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @returns {[number, number]}
 */
const getFiveDiceWinCnt = (aDice, bDice) => {
  const aSumCase = [];
  const bSumCase = [];
  for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
      for (var k = 0; k < 6; k++) {
        for (var l = 0; l < 6; l++) {
          for (var m = 0; m < 6; m++) {
            aSumCase.push(
              aDice[0][i] +
                aDice[1][j] +
                aDice[2][k] +
                aDice[3][l] +
                aDice[4][m]
            );
            bSumCase.push(
              bDice[0][i] +
                bDice[1][j] +
                bDice[2][k] +
                bDice[3][l] +
                bDice[4][m]
            );
          }
        }
      }
    }
  }
  return getOneDiceWinCnt(aSumCase, bSumCase);
};

/**
 * @param {number[][]} aDice
 * @param {number[][]} bDice
 * @param {number} cnt
 * @returns {[number, number]}
 */
const getWinnerAndCnt = (aDice, bDice, cnt) => {
  if (cnt === 1) return getOneDiceWinCnt(aDice, bDice);
  if (cnt === 2) return getTwoDiceWinCnt(aDice, bDice);
  if (cnt === 3) return getThreeDiceWinCnt(aDice, bDice);
  if (cnt === 4) return getFourDiceWinCnt(aDice, bDice);
  if (cnt === 5) return getFiveDiceWinCnt(aDice, bDice);
};

/**
 * @param {number[][]} dice
 * @returns {number[]}
 */
function solution(dice) {
  let aDiceCase = [[]];
  let bDiceCase = [[]];
  const diceLength = dice.length;
  switch (diceLength) {
    case 2:
      aDiceCase = [[0]];
      bDiceCase = [[1]];
      break;
    case 4:
      aDiceCase = [
        [0, 1],
        [0, 2],
        [0, 3],
      ];
      bDiceCase = [
        [1, 2],
        [1, 3],
        [2, 3],
      ];
      break;
    case 6:
      aDiceCase = [
        [0, 1, 2],
        [0, 1, 3],
        [0, 1, 4],
        [0, 1, 5],
        [0, 2, 3],
        [0, 2, 4],
        [0, 2, 5],
        [0, 3, 4],
        [0, 3, 5],
        [0, 4, 5],
      ];
      bDiceCase = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5],
      ];
      break;
    case 8:
      aDiceCase = [
        [0, 1, 2, 3],
        [0, 1, 2, 4],
        [0, 1, 2, 5],
        [0, 1, 2, 6],
        [0, 1, 2, 7],
        [0, 1, 3, 4],
        [0, 1, 3, 5],
        [0, 1, 3, 6],
        [0, 1, 3, 7],
        [0, 1, 4, 5],
        [0, 1, 4, 6],
        [0, 1, 4, 7],
        [0, 1, 5, 6],
        [0, 1, 5, 7],
        [0, 1, 6, 7],
        [0, 2, 3, 4],
        [0, 2, 3, 5],
        [0, 2, 3, 6],
        [0, 2, 3, 7],
        [0, 2, 4, 5],
        [0, 2, 4, 6],
        [0, 2, 4, 7],
        [0, 2, 5, 6],
        [0, 2, 5, 7],
        [0, 2, 6, 7],
        [0, 3, 4, 5],
        [0, 3, 4, 6],
        [0, 3, 4, 7],
        [0, 3, 5, 6],
        [0, 3, 5, 7],
        [0, 3, 6, 7],
        [0, 4, 5, 6],
        [0, 4, 5, 7],
        [0, 4, 6, 7],
        [0, 5, 6, 7],
      ];
      bDiceCase = [
        [1, 2, 3, 4],
        [1, 2, 3, 5],
        [1, 2, 3, 6],
        [1, 2, 3, 7],
        [1, 2, 4, 5],
        [1, 2, 4, 6],
        [1, 2, 4, 7],
        [1, 2, 5, 6],
        [1, 2, 5, 7],
        [1, 2, 6, 7],
        [1, 3, 4, 5],
        [1, 3, 4, 6],
        [1, 3, 4, 7],
        [1, 3, 5, 6],
        [1, 3, 5, 7],
        [1, 3, 6, 7],
        [1, 4, 5, 6],
        [1, 4, 5, 7],
        [1, 4, 6, 7],
        [1, 5, 6, 7],
        [2, 3, 4, 5],
        [2, 3, 4, 6],
        [2, 3, 4, 7],
        [2, 3, 5, 6],
        [2, 3, 5, 7],
        [2, 3, 6, 7],
        [2, 4, 5, 6],
        [2, 4, 5, 7],
        [2, 4, 6, 7],
        [2, 5, 6, 7],
        [3, 4, 5, 6],
        [3, 4, 5, 7],
        [3, 4, 6, 7],
        [3, 5, 6, 7],
        [4, 5, 6, 7],
      ];
      break;
    case 10:
      aDiceCase = [
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 5],
        [0, 1, 2, 3, 6],
        [0, 1, 2, 3, 7],
        [0, 1, 2, 3, 8],
        [0, 1, 2, 3, 9],
        [0, 1, 2, 4, 5],
        [0, 1, 2, 4, 6],
        [0, 1, 2, 4, 7],
        [0, 1, 2, 4, 8],
        [0, 1, 2, 4, 9],
        [0, 1, 2, 5, 6],
        [0, 1, 2, 5, 7],
        [0, 1, 2, 5, 8],
        [0, 1, 2, 5, 9],
        [0, 1, 2, 6, 7],
        [0, 1, 2, 6, 8],
        [0, 1, 2, 6, 9],
        [0, 1, 2, 7, 8],
        [0, 1, 2, 7, 9],
        [0, 1, 2, 8, 9],
        [0, 1, 3, 4, 5],
        [0, 1, 3, 4, 6],
        [0, 1, 3, 4, 7],
        [0, 1, 3, 4, 8],
        [0, 1, 3, 4, 9],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 5, 7],
        [0, 1, 3, 5, 8],
        [0, 1, 3, 5, 9],
        [0, 1, 3, 6, 7],
        [0, 1, 3, 6, 8],
        [0, 1, 3, 6, 9],
        [0, 1, 3, 7, 8],
        [0, 1, 3, 7, 9],
        [0, 1, 3, 8, 9],
        [0, 1, 4, 5, 6],
        [0, 1, 4, 5, 7],
        [0, 1, 4, 5, 8],
        [0, 1, 4, 5, 9],
        [0, 1, 4, 6, 7],
        [0, 1, 4, 6, 8],
        [0, 1, 4, 6, 9],
        [0, 1, 4, 7, 8],
        [0, 1, 4, 7, 9],
        [0, 1, 4, 8, 9],
        [0, 1, 5, 6, 7],
        [0, 1, 5, 6, 8],
        [0, 1, 5, 6, 9],
        [0, 1, 5, 7, 8],
        [0, 1, 5, 7, 9],
        [0, 1, 5, 8, 9],
        [0, 1, 6, 7, 8],
        [0, 1, 6, 7, 9],
        [0, 1, 6, 8, 9],
        [0, 1, 7, 8, 9],
        [0, 2, 3, 4, 5],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 4, 7],
        [0, 2, 3, 4, 8],
        [0, 2, 3, 4, 9],
        [0, 2, 3, 5, 6],
        [0, 2, 3, 5, 7],
        [0, 2, 3, 5, 8],
        [0, 2, 3, 5, 9],
        [0, 2, 3, 6, 7],
        [0, 2, 3, 6, 8],
        [0, 2, 3, 6, 9],
        [0, 2, 3, 7, 8],
        [0, 2, 3, 7, 9],
        [0, 2, 3, 8, 9],
        [0, 2, 4, 5, 6],
        [0, 2, 4, 5, 7],
        [0, 2, 4, 5, 8],
        [0, 2, 4, 5, 9],
        [0, 2, 4, 6, 7],
        [0, 2, 4, 6, 8],
        [0, 2, 4, 6, 9],
        [0, 2, 4, 7, 8],
        [0, 2, 4, 7, 9],
        [0, 2, 4, 8, 9],
        [0, 2, 5, 6, 7],
        [0, 2, 5, 6, 8],
        [0, 2, 5, 6, 9],
        [0, 2, 5, 7, 8],
        [0, 2, 5, 7, 9],
        [0, 2, 5, 8, 9],
        [0, 2, 6, 7, 8],
        [0, 2, 6, 7, 9],
        [0, 2, 6, 8, 9],
        [0, 2, 7, 8, 9],
        [0, 3, 4, 5, 6],
        [0, 3, 4, 5, 7],
        [0, 3, 4, 5, 8],
        [0, 3, 4, 5, 9],
        [0, 3, 4, 6, 7],
        [0, 3, 4, 6, 8],
        [0, 3, 4, 6, 9],
        [0, 3, 4, 7, 8],
        [0, 3, 4, 7, 9],
        [0, 3, 4, 8, 9],
        [0, 3, 5, 6, 7],
        [0, 3, 5, 6, 8],
        [0, 3, 5, 6, 9],
        [0, 3, 5, 7, 8],
        [0, 3, 5, 7, 9],
        [0, 3, 5, 8, 9],
        [0, 3, 6, 7, 8],
        [0, 3, 6, 7, 9],
        [0, 3, 6, 8, 9],
        [0, 3, 7, 8, 9],
        [0, 4, 5, 6, 7],
        [0, 4, 5, 6, 8],
        [0, 4, 5, 6, 9],
        [0, 4, 5, 7, 8],
        [0, 4, 5, 7, 9],
        [0, 4, 5, 8, 9],
        [0, 4, 6, 7, 8],
        [0, 4, 6, 7, 9],
        [0, 4, 6, 8, 9],
        [0, 4, 7, 8, 9],
        [0, 5, 6, 7, 8],
        [0, 5, 6, 7, 9],
        [0, 5, 6, 8, 9],
        [0, 5, 7, 8, 9],
        [0, 6, 7, 8, 9],
      ];
      bDiceCase = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 6],
        [1, 2, 3, 4, 7],
        [1, 2, 3, 4, 8],
        [1, 2, 3, 4, 9],
        [1, 2, 3, 5, 6],
        [1, 2, 3, 5, 7],
        [1, 2, 3, 5, 8],
        [1, 2, 3, 5, 9],
        [1, 2, 3, 6, 7],
        [1, 2, 3, 6, 8],
        [1, 2, 3, 6, 9],
        [1, 2, 3, 7, 8],
        [1, 2, 3, 7, 9],
        [1, 2, 3, 8, 9],
        [1, 2, 4, 5, 6],
        [1, 2, 4, 5, 7],
        [1, 2, 4, 5, 8],
        [1, 2, 4, 5, 9],
        [1, 2, 4, 6, 7],
        [1, 2, 4, 6, 8],
        [1, 2, 4, 6, 9],
        [1, 2, 4, 7, 8],
        [1, 2, 4, 7, 9],
        [1, 2, 4, 8, 9],
        [1, 2, 5, 6, 7],
        [1, 2, 5, 6, 8],
        [1, 2, 5, 6, 9],
        [1, 2, 5, 7, 8],
        [1, 2, 5, 7, 9],
        [1, 2, 5, 8, 9],
        [1, 2, 6, 7, 8],
        [1, 2, 6, 7, 9],
        [1, 2, 6, 8, 9],
        [1, 2, 7, 8, 9],
        [1, 3, 4, 5, 6],
        [1, 3, 4, 5, 7],
        [1, 3, 4, 5, 8],
        [1, 3, 4, 5, 9],
        [1, 3, 4, 6, 7],
        [1, 3, 4, 6, 8],
        [1, 3, 4, 6, 9],
        [1, 3, 4, 7, 8],
        [1, 3, 4, 7, 9],
        [1, 3, 4, 8, 9],
        [1, 3, 5, 6, 7],
        [1, 3, 5, 6, 8],
        [1, 3, 5, 6, 9],
        [1, 3, 5, 7, 8],
        [1, 3, 5, 7, 9],
        [1, 3, 5, 8, 9],
        [1, 3, 6, 7, 8],
        [1, 3, 6, 7, 9],
        [1, 3, 6, 8, 9],
        [1, 3, 7, 8, 9],
        [1, 4, 5, 6, 7],
        [1, 4, 5, 6, 8],
        [1, 4, 5, 6, 9],
        [1, 4, 5, 7, 8],
        [1, 4, 5, 7, 9],
        [1, 4, 5, 8, 9],
        [1, 4, 6, 7, 8],
        [1, 4, 6, 7, 9],
        [1, 4, 6, 8, 9],
        [1, 4, 7, 8, 9],
        [1, 5, 6, 7, 8],
        [1, 5, 6, 7, 9],
        [1, 5, 6, 8, 9],
        [1, 5, 7, 8, 9],
        [1, 6, 7, 8, 9],
        [2, 3, 4, 5, 6],
        [2, 3, 4, 5, 7],
        [2, 3, 4, 5, 8],
        [2, 3, 4, 5, 9],
        [2, 3, 4, 6, 7],
        [2, 3, 4, 6, 8],
        [2, 3, 4, 6, 9],
        [2, 3, 4, 7, 8],
        [2, 3, 4, 7, 9],
        [2, 3, 4, 8, 9],
        [2, 3, 5, 6, 7],
        [2, 3, 5, 6, 8],
        [2, 3, 5, 6, 9],
        [2, 3, 5, 7, 8],
        [2, 3, 5, 7, 9],
        [2, 3, 5, 8, 9],
        [2, 3, 6, 7, 8],
        [2, 3, 6, 7, 9],
        [2, 3, 6, 8, 9],
        [2, 3, 7, 8, 9],
        [2, 4, 5, 6, 7],
        [2, 4, 5, 6, 8],
        [2, 4, 5, 6, 9],
        [2, 4, 5, 7, 8],
        [2, 4, 5, 7, 9],
        [2, 4, 5, 8, 9],
        [2, 4, 6, 7, 8],
        [2, 4, 6, 7, 9],
        [2, 4, 6, 8, 9],
        [2, 4, 7, 8, 9],
        [2, 5, 6, 7, 8],
        [2, 5, 6, 7, 9],
        [2, 5, 6, 8, 9],
        [2, 5, 7, 8, 9],
        [2, 6, 7, 8, 9],
        [3, 4, 5, 6, 7],
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 9],
        [3, 4, 5, 7, 8],
        [3, 4, 5, 7, 9],
        [3, 4, 5, 8, 9],
        [3, 4, 6, 7, 8],
        [3, 4, 6, 7, 9],
        [3, 4, 6, 8, 9],
        [3, 4, 7, 8, 9],
        [3, 5, 6, 7, 8],
        [3, 5, 6, 7, 9],
        [3, 5, 6, 8, 9],
        [3, 5, 7, 8, 9],
        [3, 6, 7, 8, 9],
        [4, 5, 6, 7, 8],
        [4, 5, 6, 7, 9],
        [4, 5, 6, 8, 9],
        [4, 5, 7, 8, 9],
        [4, 6, 7, 8, 9],
        [5, 6, 7, 8, 9],
      ];
      break;
  }
  let answer = [];
  let winCnt = 0;
  for (var i = 0; i < aDiceCase.length; i++) {
    const bCase = [];
    const aCase = dice.filter((item, idx) => {
      const isIn = aDiceCase[i].includes(idx);
      if (!isIn) bCase.push(dice[idx]);
      return isIn;
    });

    const [nowWinCnt, whoIsWin] = getWinnerAndCnt(aCase, bCase, diceLength / 2);
    if (winCnt < nowWinCnt) {
      winCnt = nowWinCnt;
      if (whoIsWin === 0) {
        answer = aDiceCase[i].map((item) => item + 1);
      } else {
        answer = bDiceCase[i].map((item) => item + 1);
      }
    }
  }
  return answer;
}
