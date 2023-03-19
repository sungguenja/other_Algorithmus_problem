function solution(n, m, section) {
  var answer = 0;
  var sectionIndex = 0;
  while (sectionIndex < section.length) {
    const nowPrint = section[sectionIndex];
    const startIndex = sectionIndex;

    for (
      var nextIndex = sectionIndex;
      nextIndex < section.length;
      nextIndex++
    ) {
      const nextSection = section[nextIndex];

      if (nextSection >= nowPrint + m) break;

      sectionIndex = nextIndex + 1;
    }

    answer++;
  }
  return answer;
}
