const fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
// let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const N = input[0]
const arr = input.slice(1).map((line) => Array.from(line))
const visited = Array.from({ length:N }, () => Array.from({ length:N }, () => false))

const dy = [-1, 0, 1, 0]
const dx = [0, 1, 0, -1]

const answer = [0,[]]

function dfs(y,x) {
  const stk_y = [y]
  const stk_x = [x]
  let cnt = 0
  visited[y][x] = true
  while (stk_x.length > 0) {
    y = stk_y.pop()
    x = stk_x.pop()
    cnt += 1
    for (let i = 0; i < 4; i++) {
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && arr[ny][nx] == 1) {
        stk_y.push(ny)
        stk_x.push(nx)
        visited[ny][nx] = true
      }
    }
  }
  answer[0] += 1
  answer[1].push(cnt)
}

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (!visited[y][x] && arr[y][x] == 1) {
      dfs(y,x)
    }
  }
}

answer[1].sort((a,b) => (a-b))

console.log(answer[0])
for (const element of answer[1]) {
  console.log(element)
}