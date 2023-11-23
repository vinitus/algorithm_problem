const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [NM, MInputArr, ...inputArr] = input.split('\n');

  const [N, M] = NM.split(' ').map(Number);
  const travelArr = MInputArr.split(' ').map(Number);

  const costArr = inputArr.reduce(
    (prev, line, idx) => {
      prev[idx] = line.split(' ').map(Number);
      return prev;
    },
    Array.from({ length: N - 1 }),
    () => Array(3).fill(0)
  );

  const railroadInfo = Array.from({ length: N + 1 }, () => 0);

  for (let m = 0; m < M - 1; m += 1) {
    if (travelArr[m] < travelArr[m + 1]) {
      railroadInfo[travelArr[m]] += 1;
      railroadInfo[travelArr[m + 1]] -= 1;
      continue;
    }
    railroadInfo[travelArr[m]] -= 1;
    railroadInfo[travelArr[m + 1]] += 1;
  }

  let result = 0;
  let prefixSum = 0;

  for (let idx = 0; idx < N - 1; idx += 1) {
    prefixSum += railroadInfo[idx + 1];
    result += Math.min(costArr[idx][0] * prefixSum, costArr[idx][1] * prefixSum + costArr[idx][2]);
  }

  return result;
}

console.log(main(input));

module.exports = main;
