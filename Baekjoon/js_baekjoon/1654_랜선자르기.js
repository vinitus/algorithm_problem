const fs = require('fs');
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const [K, N] = input[0].split(" ")
const arr = input.slice(1).map(Number)

let s = 0
let e = Math.max.apply(null, arr)

while (s <= e) {
  let m = Math.floor((s+e) / 2)
  if (m === 0) {
    break
  }
  let cnt = 0
  for (const element of arr) {
    cnt += Math.floor(element / m)
  }
  if (cnt >= N) {
    s = m + 1
  } else {
    e = m - 1
  }
}

console.log(e)