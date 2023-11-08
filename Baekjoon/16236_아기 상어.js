const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [strN, ...inputArr] = input.split('\n');
  const N = Number(strN);
  const fishbowl = inputArr.map((item) => item.split(' ').map(Number));

  let shark = {
    position: [0, 0],
    size: 2,
    growth: 0,
    sharkGrowUp() {
      this.growth += 1;
      if (this.growth >= this.size) {
        this.growth = 0;
        this.size += 1;
      }
    },
  };

  findShark(N, (x, y) => {
    if (fishbowl[y][x] === 9) {
      shark.position = [y, x];
      fishbowl[y][x] = 0;
    }
  });

  let result = 0;

  while (true) {
    const bfsResult = bfs(fishbowl, shark, N);
    if (!bfsResult) break;
    const [time, [y, x]] = bfsResult;
    fishbowl[y][x] = 0;
    shark.position = [y, x];
    shark.sharkGrowUp();
    result += time;
  }

  return result;
}

function bfs(arr, shark, N) {
  const visited = Array.from(Array(N), () => Array(N).fill(false));

  const q = [[...shark.position, 0]];

  const d = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const minTarget = {
    distance: 20 * 20 + 1,
    positionArr: [],
  };

  while (q.length > 0) {
    const [y, x, distance] = q.shift();

    for (const [dy, dx] of d) {
      const ny = y + dy;
      const nx = x + dx;

      if (0 > ny || ny >= N || 0 > nx || nx >= N) continue;

      if (visited[ny][nx]) continue;

      if (arr[ny][nx] > shark.size) continue;

      if (arr[ny][nx] === 0) {
        q.push([ny, nx, distance + 1]);
        visited[ny][nx] = true;
        continue;
      }

      if (arr[ny][nx] === shark.size) {
        q.push([ny, nx, distance + 1]);
        visited[ny][nx] = true;
        continue;
      }

      if (minTarget.distance > distance + 1) {
        minTarget.distance = distance + 1;
        minTarget.positionArr = [[ny, nx]];
        visited[ny][nx] = true;
        continue;
      }

      if (minTarget.distance === distance + 1) {
        minTarget.positionArr.push([ny, nx]);
        visited[ny][nx] = true;
      }
    }
  }

  return minTarget.positionArr.length
    ? [
        minTarget.distance,
        minTarget.positionArr.sort((a, b) => {
          if (a[0] !== b[0]) {
            return a[0] - b[0];
          } else {
            return a[1] - b[1];
          }
        })[0],
      ]
    : false;
}

function findShark(N, fn) {
  for (let y = 0; y < N; y += 1) {
    for (let x = 0; x < N; x += 1) {
      fn(x, y);
    }
  }
}

console.log(main(input));

module.exports = main;
