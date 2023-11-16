const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [NH, ...inputArr] = input.split('\n');

  const [N, H] = NH.split(' ').map(Number);

  const stoneInfo = inputArr.map(Number).reduce(
    (prevStoneInfo, line, idx) => {
      if (idx % 2 === 0) prevStoneInfo.low.push(line);
      else prevStoneInfo.high.push(line);
      return prevStoneInfo;
    },
    { low: [], high: [] }
  );

  stoneInfo.low = stoneInfo.low.sort((a, b) => a - b);
  stoneInfo.high = stoneInfo.high.sort((a, b) => a - b);

  const stoneDestroyCntArr = Array(H)
    .fill(0)
    .map((item, idx) => {
      return N - lowerBinarySearch(stoneInfo.low, idx + 1) - lowerBinarySearch(stoneInfo.high, H - idx);
    });

  const minDestoryCnt = Math.min(...stoneDestroyCntArr);

  const duplicatedCnt = stoneDestroyCntArr.reduce((prevCnt, stoneDestroyCnt) => {
    if (stoneDestroyCnt === minDestoryCnt) prevCnt += 1;
    return prevCnt;
  }, 0);

  return `${minDestoryCnt} ${duplicatedCnt}`;
}

// target보다 크거나 같은 처음의 값 찾기
function lowerBinarySearch(arr, target) {
  let left = 0;
  let right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (target <= arr[mid]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }

  return left;
}

console.log(main(input));

module.exports = main;

// for (let idx = 0; idx < H; idx += 1) {
//   const destroyedStone = stoneInfo.reduce((cnt, item, inputIdx) => {
//     let isStone;
//     if (inputIdx % 2 === 1) {
//       isStone = H - item - 1 < idx;
//     } else {
//       isStone = item - 1 >= idx;
//     }
//     return isStone ? cnt + 1 : cnt;
//   }, 0);

//   if (resultObj.minCnt === destroyedStone) resultObj.sameCnt += 1;
//   else if (resultObj.minCnt > destroyedStone) {
//     resultObj.minCnt = destroyedStone;
//     resultObj.sameCnt = 1;
//   }
// }

// 0 1 0 1 0 1
// 0 1 0 1 0 0
// 0 1 0 1 1 0
// 0 1 0 0 1 0
// 0 1 1 0 1 0
// 0 0 1 0 1 0
// 1 0 1 0 1 0

// 1 5 3 3 5 1

// for h in H:
