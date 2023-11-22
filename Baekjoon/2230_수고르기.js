const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [NM, ...inputArr] = input.split('\n');
  const [N, M] = NM.split(' ').map(Number);

  const inputSet = new Set(inputArr);
  const inputNumArr = Array.from(inputSet)
    .map(Number)
    .sort((a, b) => a - b);

  let result = 2_000_000_000;
  let pointerLeft = 0;
  let pointerRight = 0;

  while (pointerLeft <= pointerRight && pointerRight < N) {
    const subResult = inputNumArr[pointerRight] - inputNumArr[pointerLeft];

    if (subResult < M) {
      pointerRight += 1;
      continue;
    }

    result = result > subResult ? subResult : result;
    pointerLeft += 1;

    if (subResult === M) break;
  }

  return result;
}

console.log(main(input));

module.exports = main;
