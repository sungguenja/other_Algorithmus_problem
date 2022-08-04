function solution(want, number, discount) {
  var answer = 0;
  const dayLength = 10;
  const wantCnt = want.length;
  for (var i = 0; i < discount.length; i++) {
    if (i + dayLength > discount.length) break;
    const discountState = discount.slice(i, i + dayLength);
    let trigger = true;
    for (var j = 0; j < wantCnt; j++) {
      if (
        number[j] <= discountState.filter((item) => want[j] === item).length
      ) {
        continue;
      } else {
        trigger = false;
        break;
      }
    }
    if (trigger) {
      answer += 1;
    }
  }
  return answer;
}

// 4번 풀고 복사해올 생각을 안함....
