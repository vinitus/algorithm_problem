const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [DP, ...inputArr] = input.split('\n');

  const [D, P] = DP.split(' ').map(Number);

  const dp = Array.from({ length: D + 1 }, () => 0);

  dp[0] = Infinity;

  for (let LC of inputArr) {
    const [L, C] = LC.split(' ').map(Number);
    for (let i = D; i >= L; i -= 1) {
      dp[i] = Math.max(dp[i], Math.min(Number(C), dp[i - Number(L)]));
    }
  }

  return dp[D];
}

console.log(main(input));

module.exports = main;
