class ReportedPerson {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.reportedCount = 0;
    this.reportPersonList = {};
  }

  reported(reporter, index) {
    if (reporter in this.reportPersonList) return;
    this.reportedCount += 1;
    this.reportPersonList[reporter] = index;
  }
}

function solution(id_list, report, k) {
  const personIndex = new Object({});
  const reportedPersonList = new Array();
  const answer = [];
  id_list.forEach((element, index) => {
    personIndex[element] = index;
    reportedPersonList.push(new ReportedPerson(element, index));
    answer.push(0);
  });

  report.forEach((item) => {
    const [reportPerson, reportedPerson] = item.split(" ");
    const reportedPersonObject =
      reportedPersonList[personIndex[reportedPerson]];
    reportedPersonObject.reported(reportPerson, personIndex[reportPerson]);
  });

  reportedPersonList.forEach((item, index) => {
    if (item.reportedCount >= k) {
      for (var reporter in item.reportPersonList) {
        answer[item.reportPersonList[reporter]] += 1;
      }
    }
  });

  return answer;
}
