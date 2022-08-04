function solution(X, Y) {
  const XSet = new Set(X.split(""));
  const XMap = new Object();
  const YMap = new Object();
  for (var i of X) {
    if (i in XMap) {
      XMap[i] += 1;
    } else {
      XMap[i] = 1;
    }
  }
  for (var i of Y) {
    if (XSet.has(i)) {
      if (i in YMap) {
        YMap[i] += 1;
      } else {
        YMap[i] = 1;
      }
    }
  }
  const YKeys = Object.keys(YMap);
  if (YKeys.length === 0) {
    return "-1";
  }
  var answer = "";
  for (var i = YKeys.length - 1; i > -1; i--) {
    const cnt =
      XMap[YKeys[i]] > YMap[YKeys[i]] ? YMap[YKeys[i]] : XMap[YKeys[i]];
    if (answer === "" && YKeys[i] === "0") {
      return "0";
    }
    answer = answer + YKeys[i].repeat(cnt);
  }

  return answer;
}
