const fs = require('fs')
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n')
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
const N = input[0].split(" ").map(Number)
const tmp_hp = [0]
const hp = tmp_hp.concat(input[1].split(" ").map(Number))
const tmp_greet = [0]
const greet = tmp_greet.concat(input[2].split(" ").map(Number))
const dp = Array.from({ length:N[0]+1 }, () =>
  Array.from({ length:101 }, () => 0)
)
for (let i = 1; i < N[0]+1; i++) {
  for (let j = 1; j < 101; j++) {
    if (hp[i] <= j && dp[i-1][j] < dp[i-1][j - hp[i]]+greet[i]) {
      dp[i][j] = dp[i-1][j - hp[i]]+greet[i]
    } else {
      dp[i][j] = dp[i-1][j]
    }
  }
}

console.log(dp[N[0]][99])