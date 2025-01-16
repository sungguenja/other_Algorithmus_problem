const DIAMOND = "diamond";
const IRON = "iron";
const STONE = "stone";
/**
 * @param {[number,number,number]} picks
 * @param {(DIAMOND | IRON | STONE)[]} minerals
 * @returns
 */
function solution(picks, minerals) {
  const mappedMinerals = [];
  const maximumMineralsArray = [];
  const maximumMineralsCntArray = [];

  const checkMineral = (diaCnt, ironCnt, stoneCnt) => {
    if (diaCnt >= ironCnt && diaCnt >= stoneCnt) {
      maximumMineralsArray.push(DIAMOND);
      maximumMineralsCntArray.push(diaCnt);
      return;
    }

    if (ironCnt >= diaCnt && ironCnt >= stoneCnt) {
      maximumMineralsArray.push(IRON);
      maximumMineralsCntArray.push(ironCnt);
      return;
    }

    maximumMineralsArray.push(STONE);
    maximumMineralsCntArray.push(stoneCnt);
  };

  var diaCnt = 0;
  var ironCnt = 0;
  var stoneCnt = 0;
  minerals.forEach((item, idx) => {
    item === DIAMOND
      ? (diaCnt += 1)
      : item === IRON
      ? (ironCnt += 1)
      : (stoneCnt += 1);
    if (idx !== 0 && idx % 5 === 4) {
      checkMineral(diaCnt, ironCnt, stoneCnt);
      mappedMinerals.push({
        diaCnt,
        ironCnt,
        stoneCnt,
      });
      diaCnt = 0;
      ironCnt = 0;
      stoneCnt = 0;
      return;
    }
    if (idx === minerals.length - 1) {
      checkMineral(diaCnt, ironCnt, stoneCnt);
      mappedMinerals.push({
        diaCnt,
        ironCnt,
        stoneCnt,
      });
    }
  });
  console.log(mappedMinerals, maximumMineralsArray, maximumMineralsCntArray);
  var answer = 0;
  return answer;
}
