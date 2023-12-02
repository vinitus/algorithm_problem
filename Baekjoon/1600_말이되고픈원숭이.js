const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [strK, WH, ...inputArr] = input.split('\n');
  const K = Number(strK);
  const [W, H] = WH.split(' ').map(Number);

  const travel = inputArr.map((line) => line.split(' ').map(Number));

  function bfs(y, x) {
    let q = [[y, x, K]];
    const horseD = [
      [-2, -1],
      [-2, 1],
      [-1, -2],
      [-1, 2],
      [1, -2],
      [1, 2],
      [2, -1],
      [2, 1],
    ];

    const visited = Array.from({ length: H }, () => {
      return Array.from({ length: W }, () => {
        return Array.from({ length: K + 1 }, () => 0);
      });
    });

    while (q.length) {
      const [y, x, nightCnt] = q.shift();

      if (y === H - 1 && x === W - 1) {
        return visited[y][x][nightCnt];
      }

      for (const [dy, dx] of [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ]) {
        const nx = x + dx;
        const ny = y + dy;

        if (0 <= ny && ny < H && 0 <= nx && nx < W && !travel[ny][nx] && !visited[ny][nx][nightCnt]) {
          q.push([ny, nx, nightCnt]);
          visited[ny][nx][nightCnt] = visited[y][x][nightCnt] + 1;
        }
      }
      if (nightCnt > 0) {
        for (const [nightDy, nightDx] of horseD) {
          const nx = x + nightDx;
          const ny = y + nightDy;

          if (0 <= ny && ny < H && 0 <= nx && nx < W && !travel[ny][nx] && !visited[ny][nx][nightCnt - 1]) {
            q.push([ny, nx, nightCnt - 1]);
            visited[ny][nx][nightCnt - 1] = visited[y][x][nightCnt] + 1;
          }
        }
      }
    }
  }

  return bfs(0, 0) ?? -1;
}

console.log(main(input));

module.exports = main;
