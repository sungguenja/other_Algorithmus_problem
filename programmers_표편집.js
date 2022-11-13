class NodeCell {
  constructor(n, prevNode, nextNode) {
    this.n = n;
    this.prevNode = prevNode;
    this.nextNode = nextNode;
  }
}

function solution(n, k, cmd) {
  const nodeArray = new Array(n).fill("O");
  const startNode = new NodeCell(0);
  let currentNode = startNode;
  let prevNode = startNode;

  for (var i = 1; i < n; i++) {
    const newNode = new NodeCell(i, prevNode);
    prevNode.nextNode = newNode;
    prevNode = newNode;

    if (i === k) {
      currentNode = newNode;
    }
  }

  const deletedHistory = [];
  const cmdLength = cmd.length;
  for (var i = 0; i < cmdLength; i++) {
    const [commandName, commandCount] = cmd[i].split(" ");
    switch (commandName) {
      case "U":
        for (var j = 0; j < commandCount; j++) {
          if (!currentNode.prevNode) {
            break;
          }
          currentNode = currentNode.prevNode;
        }
        break;
      case "D":
        for (var j = 0; j < commandCount; j++) {
          if (!currentNode.nextNode) {
            break;
          }
          currentNode = currentNode.nextNode;
        }
        break;
      case "C":
        deletedHistory.push(currentNode);
        const prevNodeC = currentNode.prevNode;
        const nextNodeC = currentNode.nextNode;
        if (prevNodeC && nextNodeC) {
          prevNodeC.nextNode = nextNodeC;
          nextNodeC.prevNode = prevNodeC;
          currentNode = nextNodeC;
        } else if (prevNodeC) {
          prevNodeC.nextNode = null;
          currentNode = prevNodeC;
        } else if (nextNodeC) {
          nextNodeC.prevNode = null;
          currentNode = nextNodeC;
        }
        break;
      case "Z":
        const restoreNode = deletedHistory.pop();
        const prevNodeZ = restoreNode.prevNode;
        const nextNodeZ = restoreNode.nextNode;
        if (prevNodeZ) {
          prevNodeZ.nextNode = restoreNode;
        }
        if (nextNodeZ) {
          nextNodeZ.prevNode = restoreNode;
        }
        break;
    }
  }

  for (var i = 0; i < deletedHistory.length; i++) {
    nodeArray[deletedHistory[i].n] = "X";
  }

  return nodeArray.join("");
}
