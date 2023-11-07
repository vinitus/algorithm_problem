const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string') return;

  const [YX, ...inputMapString] = input.split('\n');
  const [Y, X] = YX.split(' ');

  const arr = inputMapString.map((item) => item.split('').map(Number));

  const dp = arr.map((item) => [...item]);

  for (let y = 1; y < Y; y += 1) {
    for (let x = 1; x < X; x += 1) {
      if (arr[y][x] === 0) continue;

      const east = dp[y][x - 1];
      const south = dp[y - 1][x];
      const diag = dp[y - 1][x - 1];

      if (!east && !south && !diag) {
        dp[y][x] = 1;
        continue;
      }

      if (diag === south && diag === east) {
        dp[y][x] = east + 1;
      } else {
        dp[y][x] = Math.min(east, south, diag) + 1;
      }
    }
  }

  let result = 0;

  for (let y = 0; y < Y; y += 1) {
    for (let x = 0; x < X; x += 1) {
      result = result < dp[y][x] ? dp[y][x] : result;
    }
  }

  return result * result;
}

console.log(main(input));

module.exports = main;
