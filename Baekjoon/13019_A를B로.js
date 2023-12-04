const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [inputArr, target] = input.split('\n').map((line) => line.split(''));

  if (target.length !== inputArr.length) return -1;

  let idx = target.length - 1;
  let result = 0;

  for (let i = target.length - 1; i > -1; i -= 1) {
    if (inputArr[i] !== target[idx]) result += 1;
    else idx -= 1;
  }

  if (inputArr.sort().join('') !== target.sort().join('')) return -1;

  return result;
}

console.log(main(input));

module.exports = main;
