const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  let [FF, FS, SF, SS] = input.split(' ').map(Number);

  if (FF === 0 && FS === 0) {
    return SS + (SF ? 1 : 0);
  }

  if (FF !== 0 && FS === 0) {
    return FF;
  }

  let result = FF + SS;

  // 1을 추가하는 이유는 무조건 빠른 템포만 시작하기 때문에
  // 전환하는 숫자가 달라서 그렇다
  if (FS > SF) result += 2 * SF + 1;
  else result += 2 * FS;

  return result;
}

console.log(main(input));

module.exports = main;
