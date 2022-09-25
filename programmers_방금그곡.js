class Music {
  constructor(information) {
    const [startTime, endTime, musicTitle, scale] = information.split(",");
    const [startHour, startMinute] = startTime.split(":");
    const [endHour, endMinute] = endTime.split(":");
    this.startTime = Number(startHour) * 60 + Number(startMinute);
    this.endTime = Number(endHour) * 60 + Number(endMinute);
    this.musicDuring = this.endTime - this.startTime;
    this.title = musicTitle;
    this.scale = [];
    let i = 0;
    let j = 0;
    while (i < this.musicDuring) {
      i++;
      this.scale.push(scale[j % scale.length]);
      j++;
      if (scale[j % scale.length] == "#") {
        this.scale[this.scale.length - 1] += "#";
        j++;
      }
    }
  }
}

function isSong(mine, scale) {
  let i = 0;
  let mine_string = mine.join("");
  while (i < scale.length) {
    if (mine[0] != scale[i]) i += 1;
    else {
      if (mine_string == scale.slice(i, i + mine.length).join("")) return true;
      i += 1;
    }
  }
  return false;
}

function solution(m, musicinfos) {
  const scaleList = [];
  for (var i = 0; i < m.length; i++) {
    if (i === "#") scaleList[scaleList.length - 1] += i;
    else scaleList.push(m[i]);
  }
  for (var i = 0; i < musicinfos.length; i++) {
    musicinfos[i] = new Music(musicinfos[i]);
  }
  const mArray = scaleList.slice();
  let answer = "(None)";
  let answerTime = -1;
  let startTime = -1;

  musicinfos.forEach((item) => {
    if (isSong(mArray, item.scale)) {
      if (answerTime < item.musicDuring) {
        answerTime = item.musicDuring;
        answer = item.title;
        startTime = item.startTime;
      } else if (answerTime == item.musicDuring) {
        if (startTime > item.startTime) {
          answerTime = item.musicDuring;
          answer = item.title;
          startTime = item.startTime;
        }
      }
    }
  });
  return answer;
}
