function gcd(a, b) {
  var result = -1;
  const endPoint = Math.min(a, b);
  for (var i = 0; i < endPoint + 1; i++) {
    if (a % i === 0 && b % i === 0) {
      result = i;
    }
  }
  return result;
}

function solution(w, h) {
  var answer = w * h - (w + h - gcd(w, h));
  return answer;
}
