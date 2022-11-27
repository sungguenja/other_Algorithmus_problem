const makeObject = (want, length) => {
  const tmpObj = new Object();
  for (var i = 0; i < length; i++) {
    tmpObj[want[i]] = i;
  }
  return tmpObj;
};

function solution(want, number, discount) {
  var answer = 0;
  const length = want.length;
  const sumCnt = 10;
  const cntArray = new Array(length);
  const discountLength = discount.length;
  const wantObj = makeObject(want, length);
  var left = 0;
  for (var right = 0; right < discountLength; right++) {
    if (right < sumCnt) {
      if (wantObj[discount[right]] !== undefined) {
        cntArray[wantObj[discount[right]]] =
          cntArray[wantObj[discount[right]]] === undefined
            ? 1
            : cntArray[wantObj[discount[right]]] + 1;
      }
      for (var j = 0; j < length; j++) {
        if (cntArray[j] !== number[j]) {
          break;
        }
      }
      if (j === length) {
        answer++;
      }
      continue;
    }

    if (
      wantObj[discount[left]] !== undefined &&
      cntArray[wantObj[discount[left]]] !== undefined
    ) {
      cntArray[wantObj[discount[left]]] = cntArray[wantObj[discount[left]]] - 1;
    }

    if (wantObj[discount[right]] !== undefined) {
      cntArray[wantObj[discount[right]]] =
        cntArray[wantObj[discount[right]]] === undefined
          ? 1
          : cntArray[wantObj[discount[right]]] + 1;
    }

    for (var j = 0; j < length; j++) {
      if (cntArray[j] !== number[j]) {
        break;
      }
    }
    if (j === length) {
      answer++;
    }

    left++;
  }
  return answer;
}
