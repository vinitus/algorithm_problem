const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const N = input[0]
const lst = input.slice(1).map((row) => row.split(" ").map(Number))

function dfs(idx) {
  const visited = Array.from({ length:N }, () => false)
  const stk = [idx]
  
  while (stk.length > 0) {
    let now = stk.pop()
    for (let x = 0; x < N; x++) {
      if (lst[now][x] == 1 && !visited[x]) {
        stk.push(x)
        visited[x] = true
        lst[idx][x] = 1
      }
    }
  }
}

for (let i = 0; i < N; i++) {
  dfs(i)
}

let result = "";
lst.forEach(function (row) {
  result += row.join(" ") + "\n"
})

console.log(result)