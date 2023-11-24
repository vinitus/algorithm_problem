const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [VE, ...nodeInfoStr] = input.split('\n');
  const [V, E] = VE.split(' ').map(Number);
  const nodeInfo = nodeInfoStr.reduce(
    (prev, line) => {
      const [y, x, d] = line.split(' ').map(Number);
      prev[y][x] = d;
      return prev;
    },
    Array.from({ length: V + 1 }, () => Array.from({ length: V + 1 }, () => Infinity))
  );

  for (let middle = 1; middle <= V; middle++) {
    for (let start = 1; start <= V; start++) {
      for (let end = 1; end <= V; end++) {
        nodeInfo[start][end] = Math.min(nodeInfo[start][end], nodeInfo[start][middle] + nodeInfo[middle][end]);
      }
    }
  }

  let result = Infinity;

  for (let i = 1; i <= V; i += 1) {
    result = result > nodeInfo[i][i] ? nodeInfo[i][i] : result;
  }

  return result === Infinity ? -1 : result;
}

console.log(main(input));

module.exports = main;
