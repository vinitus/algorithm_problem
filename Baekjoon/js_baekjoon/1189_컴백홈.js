const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const [R, C, K] = input[0].split(" ") // R, C, K 구분

const dy = [-1, 0, 1, 0]
const dx = [0, 1, 0, -1]

const visited = Array.from({ length: R}, () =>
  Array.from({ length:C }, () => false)
)
// list(list(False for _ in range(C)) for _ in range(R))
// R번 array를 만들기를 반복하는데 C번 또 반복함, 넣는 인자는 => 를 통해서 넣는다

const arr = input.slice(1) // 1 index부터 slice
let answer = 0

function dfs(y, x, cnt) {
  visited[y][x] = true
  if (y == 0 && x == C - 1) {
    if (cnt == K) {
        answer += 1
        return
    }
  }

  for (let i = 0; i < 4; i++) {
    let ny = y + dy[i]
    let nx = x + dx[i]
    if (0 <= ny && ny < R && 0 <= nx && nx < C && !visited[ny][nx] && arr[ny][nx] != "T") {
      visited[ny][nx] = true
      dfs(ny, nx, cnt + 1)
      visited[ny][nx] = false
    }
  }
}

dfs(R - 1, 0, 1)

console.log(answer)