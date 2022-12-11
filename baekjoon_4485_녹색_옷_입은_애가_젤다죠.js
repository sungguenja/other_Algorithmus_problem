const answer = [];

const caveFunction = (size, cave) => {
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  const visit = new Array(size);
  for (var i = 0; i < size; i++) {
    visit.push(new Array(size));
  }

  const Que = [[0, 0, cave[0][0]]];
  while (Que.length > 0) {
    const [i, j, ruppy] = Que.pop();
    for (var k = 0; k < 4; k++) {
      const ni = i + di[k];
      const nj = j + dj[k];
      if (0 <= ni && ni < size && 0 <= nj && nj < size) {
        if (
          visit[ni][nj] === undefined ||
          ruppy + cave[ni][nj] < visit[ni][nj]
        ) {
          visit[ni][nj] = ruppy + cave[ni][nj];
          Que.push([ni, nj, ruppy + cave[ni][nj]]);
        }
      }
    }
  }
  return visit[size - 1][size - 1];
};

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let trigger = true;
let i = 0;

while (trigger) {
  const size = input[i];
  if (size === "0") {
    trigger = true;
    break;
  }
  answer.push(caveFunction(size, input.slice(i + 1, i + size)));
  i += size;
}

for (var ans = 0; ans < answer.length; ans++) {
  console.log(`Problem ${ans + 1}: ${answer[ans]}`);
}
