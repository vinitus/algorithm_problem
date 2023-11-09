const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [NM, WM, ...arr] = input.split('\n');

  const [N, M] = NM.split(' ').map(Number);
  const univInfo = WM.split(' ');

  const graph = arr
    .reduce((prev, curr) => {
      const [u, v, d] = curr.split(' ').map(Number);
      prev.push([d, u - 1, v - 1]);

      return prev;
    }, [])
    .sort((a, b) => {
      for (let i = 0; i < 3; i += 1) {
        if (a[i] === b[i]) continue;
        return a[i] - b[i];
      }
    });

  let answer = 0;
  let cnt = 0;

  const parent = Array.from(Array(N), (_, i) => i);

  for (const [d, u, v] of graph) {
    if (univInfo[u] !== univInfo[v] && findParent(parent, u) !== findParent(parent, v)) {
      union(parent, u, v);
      answer += d;
      cnt += 1;
    }
    if (cnt === N - 1) break;
  }

  if (cnt !== N - 1) return -1;

  return answer;
}

function findParent(parent, i) {
  if (parent[i] != i) parent[i] = findParent(parent, parent[i]);
  return parent[i];
}

function union(parent, i, j) {
  const first = findParent(parent, i);
  const second = findParent(parent, j);
  if (first < second) parent[second] = first;
  else parent[first] = second;
}

console.log(main(input));

module.exports = main;
