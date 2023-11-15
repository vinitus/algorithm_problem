const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [stringN, ...inputArr] = input.split('\n');

  const N = Number(stringN);

  // 부모노드 자식노드 가중치
  const tree = inputArr.reduce(
    (tree, line) => {
      const [parent, child, weight] = line.split(' ').map(Number);

      tree[parent].push([child, weight]);
      tree[child].push([parent, weight]);

      return tree;
    },
    Array.from({ length: N + 1 }, () => [])
  );

  const firstBFSNode = bfs(tree, 1, N + 1);

  return bfs(tree, firstBFSNode.node, N + 1).weight;
}

function bfs(arr, s, N) {
  const q = [[s, 0]];
  const visited = Array(N).fill(false);
  const maxLengthNodeObj = {
    node: 0,
    weight: 0,
    update(node, weight) {
      if (this.weight >= weight) return;

      this.weight = weight;
      this.node = node;
    },
  };

  while (q.length > 0) {
    const [node, weight] = q.shift();

    if (visited[node]) continue;

    visited[node] = true;
    maxLengthNodeObj.update(node, weight);

    arr[node]?.forEach(([childNode, childWeight]) => {
      q.push([childNode, childWeight + weight]);
    });
  }

  return maxLengthNodeObj;
}

console.log(main(input));

module.exports = main;
