function solution(k, d) {
  var answer = 0;
  for (var i = 0; i <= d; i += k) {
    const maxY = parseInt((d ** 2 - i ** 2) ** (1 / 2));
    answer += parseInt(maxY / k) + 1;
  }
  return answer;
}
