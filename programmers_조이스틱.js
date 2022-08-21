function solution(name) {
  let answer = 0;
  let min = name.length - 1;

  for (let i = 0; i < name.length; i++) {
    const charCodeNumber = name.charCodeAt(i);

    if (charCodeNumber < 78) {
      answer += charCodeNumber - 65;
    } else {
      answer += 91 - charCodeNumber;
    }

    let nextIndex = i + 1;
    while (nextIndex < name.length && name[nextIndex] === "A") {
      nextIndex++;
    }

    min = Math.min(min, i * 2 + name.length - nextIndex);
    min = Math.min(min, (name.length - nextIndex) * 2 + i);
  }
  return answer + min;
}
