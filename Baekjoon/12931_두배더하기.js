const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  let [N, targetArr] = input.split('\n');
  N = Number(N);
  targetArr = targetArr
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);

  let result = 0;

  while (targetArr[N - 1] !== 0) {
    const tmpArr = [];
    let flag = false;
    for (let i = 0; i < N; i += 1) {
      const nowNum = targetArr[i];
      if (nowNum % 2 === 1) {
        targetArr[i] = nowNum - 1;
        result += 1;
        flag = true;
        break;
      }
      tmpArr.push(nowNum / 2);
    }

    if (!flag) {
      targetArr = [...tmpArr];
      result += 1;
    }
  }

  return result;
}

console.log(main(input));

module.exports = main;
