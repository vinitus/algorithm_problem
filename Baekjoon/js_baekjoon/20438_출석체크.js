const fs = require('fs')
// let input = fs.readFileSync('./input.txt').toString().trim().split('\n')
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')

const [NN, K, Q, M] = input[0].split(" ").map(Number)
const sleep = input[1].split(" ").map(Number)
const check = input[2].split(" ").map(Number)
const gugan = input.splice(3)
const N = NN + 3
const student = Array.from({ length:N }, () => 0)

for (let i = 0; i < K; i++) {
  student[sleep[i]] = 2
}

for (const checkStu of check) {
  if (student[checkStu] != 2) {
    for (let k = checkStu; k < N; k+=checkStu) {
      if (student[k] != 2) {
      student[k] = 1
      }
    }
  }
}

for (let i = 3; i < N; i++) {
  if (student[i] != 2) {
    student[i] += student[i-1]
  } else {
    student[i] = student[i-1]
  }
}

let answer = ""
for (const range of gugan) {
  const [s, e] = range.split(" ").map(Number)
  answer += `${e - s + 1 - student[e] + student[s-1]}\n`
}
console.log(answer)