const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [strT, ...NM] = input.split('\n');
  const T = Number(strT);
  const result = [];

  for (let t = 0; t < T; t += 1) {
    const [N, M] = NM[t].split(' ').map(Number);
    const dp = Array.from({ length: N }, () => Array.from({ length: M + 1 }, () => 0));

    for (let idx = 0; idx < M + 1; idx += 1) {
      dp[0][idx] = idx;
    }

    for (let cnt = 1; cnt < N; cnt += 1) {
      for (let idx = 1; idx < M + 1; idx += 1) {
        dp[cnt][idx] = dp[cnt][idx - 1] + dp[cnt - 1][Math.floor(idx / 2)];
      }
    }

    result.push(dp[N - 1][M].toString());
  }

  return result.join('\n');
}

console.log(main(input));

module.exports = main;
