function solution(targets) {
  var answer = 0;
  targets.sort((a, b) => {
    if (a[0] === b[0]) return a[1] - b[1];
    return a[0] - b[0];
  });

  var nowStart = -1;
  var nowEnd = -2;

  targets.forEach((missile) => {
    if (missile[1] <= nowEnd - 1) {
      nowEnd = missile[1];
      return;
    }

    if (missile[0] <= nowEnd - 1) {
      nowStart = missile[0];
      return;
    }

    answer++;
    nowStart = missile[0];
    nowEnd = missile[1];
  });
  return answer;
}
