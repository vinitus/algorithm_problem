const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const inputArr = input.split('\n');
  const TOTAL_INDEX_END = inputArr.length;
  let totalIdx = 0;
  const result = [];

  while (totalIdx < TOTAL_INDEX_END) {
    let tmpResult = 0;
    const [N, M] = inputArr[totalIdx++].split(' ').map(Number);

    if (N === 0 && M === 0) break;

    const testcases = [];

    for (let idx = 0; idx < M; idx += 1) {
      testcases.push(inputArr[totalIdx++].split(' ').map(Number));
    }

    testcases.sort((a, b) => a[2] - b[2]);

    const parent = Array.from({ length: N }, (_, k) => k);

    function find(x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    function union(x, y) {
      let newX = find(x);
      let newY = find(y);
      if (newX < newY) {
        parent[newY] = newX;
      } else {
        parent[newX] = newY;
      }
    }

    for (const testcase of testcases) {
      const [u, v, w] = testcase;
      if (find(u) != find(v)) {
        union(u, v);
      } else {
        tmpResult += w;
      }
    }

    result.push(tmpResult);
  }

  return result.join('\n');
}

console.log(main(input));

module.exports = main;
