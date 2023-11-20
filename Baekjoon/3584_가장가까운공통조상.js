const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [T, ...inputArr] = input.split('\n');

  let totalInputIdx = 0;
  let result = [];

  for (let t = 0; t < Number(T); t += 1) {
    const N = Number(inputArr[totalInputIdx]);
    const nodeInfo = inputArr.slice(totalInputIdx + 1, totalInputIdx + N).map((line) => line.split(' ').map(Number));
    totalInputIdx += N;
    let [A, B] = inputArr[totalInputIdx].split(' ').map(Number);
    totalInputIdx += 1;

    const treeArr = nodeInfo.reduce(
      (prev, [parent, child]) => {
        prev[child] = parent;
        return prev;
      },
      Array.from({ length: N + 1 }, () => 0)
    );

    const AVisited = [0, A];
    const BVisited = [0, B];

    while (treeArr[A]) {
      AVisited.push(treeArr[A]);
      A = treeArr[A];
    }

    while (treeArr[B]) {
      BVisited.push(treeArr[B]);
      B = treeArr[B];
    }

    let visitedIdx = 1;

    while (AVisited[AVisited.length - visitedIdx] === BVisited[BVisited.length - visitedIdx]) {
      visitedIdx += 1;
    }

    result.push(AVisited[AVisited.length - visitedIdx + 1]);
  }

  return result.join('\n');
}

console.log(main(input));

module.exports = main;
