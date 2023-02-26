function solution(users, emoticons) {
  const answer = [-1, -1];
  const discountRate = [10, 20, 30, 40];
  const discountResult = [];

  const findDiscountResult = (tmp, depth) => {
    if (tmp.length == depth) {
      discountResult.push(JSON.parse(JSON.stringify(tmp)));
      return;
    }

    discountRate.forEach((item, index) => {
      const innerTmp = JSON.parse(JSON.stringify(tmp));
      innerTmp[depth] += item;
      findDiscountResult(innerTmp, depth + 1);
      innerTmp[depth] -= item;
    });
  };

  findDiscountResult(Array(emoticons.length).fill(0), 0);

  discountResult.forEach((item, index) => {
    let join = 0;
    const price = Array(users.length).fill(0);
    emoticons.forEach((emogi, emogiIndex) => {
      users.forEach((user, userIndex) => {
        if (user[0] <= item[emogiIndex]) {
          price[userIndex] += (emogi * (100 - item[emogiIndex])) / 100;
        }
      });
    });

    users.forEach((user, userIndex) => {
      if (price[userIndex] >= user[1]) {
        join += 1;
        price[userIndex] = 0;
      }
    });

    if (join >= answer[0]) {
      if (join == answer[0]) {
        answer[1] = Math.max(
          answer[1],
          price.reduce((result, now) => result + now, 0)
        );
      } else {
        answer[1] = price.reduce((result, now) => result + now, 0);
      }
      answer[0] = join;
    }
  });
  return answer;
}
