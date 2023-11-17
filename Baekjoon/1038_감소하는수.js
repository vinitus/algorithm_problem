const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const N = Number(input);

  if (N <= 9) return N;

  const numArr = Array.from({ length: 10 }, (v, k) => {
    return k;
  });

  const combinationResult = [];

  for (let i = 1; i < 11; i += 1) {
    combinationResult.push(...getCombinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], i));
  }

  const sortedArr = combinationResult.sort((a, b) => a - b);

  return sortedArr[N] ? sortedArr[N] : -1;
}

function getCombinations(arr, selectCount) {
  const results = [];

  function findCombination(temp, start, selectedCount) {
    if (selectedCount === 0) {
      results.push(
        Number(
          [...temp]
            .map(Number)
            .sort((a, b) => b - a)
            .join('')
        )
      );
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      findCombination(temp, i + 1, selectedCount - 1);
      temp.pop();
    }
  }

  findCombination([], 0, selectCount);
  return results;
}

console.log(main(input));

module.exports = main;
