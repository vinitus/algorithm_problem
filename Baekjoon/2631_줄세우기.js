const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [N, ...inputArr] = input.split('\n').map(Number);

  return N - findMaxSubSequence(inputArr);
}

console.log(main(input));

module.exports = main;

function findMaxSubSequence(arr) {
  const n = arr.length;
  const subsequence = new Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] > arr[j] && subsequence[i] < subsequence[j] + 1) {
        subsequence[i] = subsequence[j] + 1;
      }
    }
  }

  return Math.max(...subsequence);
}
