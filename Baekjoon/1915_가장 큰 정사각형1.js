const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string') return;

  const [YX, ...inputMapString] = input.split('\n');
  const [Y, X] = YX.split(' ');

  const arr = inputMapString.map((item) => item.split('').map(Number));

  let result = 0;

  for (let y = 0; y < Y; y += 1) {
    for (let x = 0; x < X; x += 1) {
      if (arr[y][x]) {
        if (result === 0) result = 1;
        result = checkIsSquare({ X, Y, x, y, arr, maxLength: result });
      }
    }
  }

  return result * result;
}

function checkIsSquare({ x, y, maxLength, X, Y, arr }) {
  ny = y + maxLength;
  nx = x + maxLength;
  if (!isValid(nx, ny, X, Y)) return maxLength;
  return prefixSum({ X, Y, x, y, arr, maxLength });
}

function isValid(x, y, X, Y) {
  return 0 <= x && x < X && 0 <= y && y < Y;
}

function prefixSum({ x, y, X, Y, arr, maxLength }) {
  let maxX = 0;
  let maxY = 0;

  for (let nx = x; nx < X; nx += 1) {
    if (arr[y][nx] !== 1) {
      break;
    }
    maxX += 1;
  }

  for (let ny = y; ny < Y; ny += 1) {
    if (arr[ny][x] !== 1) {
      break;
    }
    maxY += 1;
  }

  let newMaxLength = maxX >= maxY ? maxY : maxX;

  if (maxLength >= newMaxLength) return maxLength;

  let calcResult = newMaxLength * newMaxLength;

  while (calcResult !== 0 && newMaxLength > maxLength) {
    calcResult = newMaxLength * newMaxLength;
    for (let nx = x; nx < x + newMaxLength; nx += 1) {
      for (let ny = y; ny < y + newMaxLength; ny += 1) {
        calcResult -= arr[ny][nx];
      }
    }
    if (calcResult !== 0) newMaxLength -= 1;
  }

  if (calcResult === 0) return newMaxLength;
  return maxLength;
}

console.log(main(input));

module.exports = main;
