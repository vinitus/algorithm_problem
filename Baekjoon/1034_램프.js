const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [NM, ...lamp] = input.split('\n');

  const [N, M] = NM.split(' ');
  const k = lamp.pop();

  return lamp.reduce((prev, item) => {
    let zeroCnt = item.split('').reduce((prev, lampState) => {
      if (lampState === '0') prev += 1;
      return prev;
    }, 0);

    let cnt = 0;
    if (zeroCnt <= k && zeroCnt % 2 === k % 2) {
      for (let i = 0; i < N; i += 1) {
        if (lamp[i] === item) cnt += 1;
      }
    }

    return prev > cnt ? prev : cnt;
  }, 0);
}

console.log(main(input));

module.exports = main;
