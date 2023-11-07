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
        const fnResult = checkIsSquare({ X, Y, x, y, arr, maxLength: result });
        if (typeof fnResult === 'number' && result < fnResult) result = fnResult;
      }
    }
  }

  return result * result;
}

function forStatement(s, e, fn) {
  for (let i = s; i < e; i += 1) {
    fn(i);
  }
}

function isValid(x, y, X, Y) {
  return 0 <= x && x < X && 0 <= y && y < Y;
}

function checkIsSquare({ x, y, maxLength, X, Y, arr }) {
  ny = y + maxLength;
  nx = x + maxLength;
  if (!isValid(nx, ny, X, Y)) return false;
  return deltaSearch({ X, Y, x, y, arr, maxLength });
}

function deltaSearch({ x, y, X, Y, arr, maxLength }) {
  const d = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
  ];

  let result = 0;
  let ey = 0;
  let ex = 0;

  for (let nx = x; nx < X; nx += 1) {
    if (arr[y][nx] === 1) {
      result += 1;
    } else {
      break;
    }
  }

  if (result <= maxLength) return false;

  let flag = true;

  while (result > maxLength && flag) {
    flag = false;
    for (let ny = y; ny < y + result; ny += 1) {
      if (isValid(x, ny, X, Y) && arr[ny][x] === 1) {
        ey = ny - y;
        ex = ny - y;
      } else {
        flag = true;
        ey = 0;
        result = ny - y;
        break;
      }
    }
  }

  if (result <= maxLength) return false;

  flag = true;

  while (result > maxLength && flag) {
    flag = false;
    for (let nx = x; nx < x + result; nx += 1) {
      if (isValid(nx, ey, X, Y) && arr[ey][nx] !== 1) {
        flag = true;
        result = ey - x;
        ey = nx - x - 1;
        ex = nx - x - 1;
        break;
      }
    }
  }

  if (result <= maxLength) return false;

  flag = true;

  while (result > maxLength && flag) {
    flag = false;
    for (let ny = y; ny < y + result; ny += 1) {
      if (isValid(ex, ny, X, Y) && arr[ny][ex] !== 1) {
        flag = true;
        result = ex - x;
        ex = ny - y - 1;
        break;
      }
    }
  }

  return result;
}

module.exports = main;
