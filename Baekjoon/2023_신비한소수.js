const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const N = Number(input);
  const result = [];

  for (let firstdigit of [2, 3, 5, 7]) {
    for (let num = firstdigit * 10 ** (N - 1); num < (firstdigit + 1) * 10 ** (N - 1); num += 1) {
      const strNum = num.toString();
      let flag = true;

      for (let i = 1; i < N; i += 1) {
        const slicedStrNum = strNum.slice(0, i + 1);

        if (!isPrime(Number(slicedStrNum))) {
          flag = false;
          break;
        }
      }

      // flag && console.log(num); // 백준 제출용
      flag && result.push(num);
    }
  }

  return result.join('\n');
}

function isPrime(num) {
  if (num < 2) return false;
  for (let idx = 2; idx * idx <= num; idx += 1) {
    if (num % idx === 0) return false;
  }
  return true;
}

console.log(main(input));

module.exports = main;
