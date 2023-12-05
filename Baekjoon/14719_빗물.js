const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [HW, inputArr] = input.split('\n');
  const [H, W] = HW.split(' ').map(Number);
  const block = inputArr.split(' ').map(Number);

  let result = 0;

  for (let idx = 1; idx < W - 1; idx += 1) {
    const left = Math.max(...block.slice(0, idx));
    const right = Math.max(...block.slice(idx + 1));
    const lowBlock = Math.min(left, right);

    if (lowBlock > block[idx]) result += lowBlock - block[idx];
  }

  return result;
}

console.log(main(input));

module.exports = main;
