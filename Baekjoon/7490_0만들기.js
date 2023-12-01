const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [T, ...inputArr] = input.split('\n');
  const result = [];

  for (let t = 0; t < T; t += 1) {
    const N = Number(inputArr[t]);
    const numArr = Array.from({ length: N }, (_, k) => k + 1);
    const bruteForce = [];

    function makeExpression(idx, str) {
      if (idx >= N) {
        bruteForce.push(str);
        return;
      }
      makeExpression(idx + 1, str + '+' + numArr[idx]);
      makeExpression(idx + 1, str + '-' + numArr[idx]);
      makeExpression(idx + 1, str + ' ' + numArr[idx]);
    }

    makeExpression(1, '1');

    bruteForce.sort().forEach((expression) => {
      const eraseSpace = expression.replaceAll(' ', '');
      let caseResult = 0;
      let idx = 0;
      while (!Number.isNaN(Number(eraseSpace[idx]))) {
        caseResult = caseResult * 10 + Number(eraseSpace[idx++]);
      }

      let prevOperator = '';
      while (idx < eraseSpace.length) {
        if (eraseSpace[idx] === '+') {
          prevOperator = '+';
          idx += 1;
        } else if (eraseSpace[idx] === '-') {
          prevOperator = '-';
          idx += 1;
        } else {
          let tmp = 0;
          while (!Number.isNaN(Number(eraseSpace[idx]))) {
            tmp = tmp * 10 + Number(eraseSpace[idx++]);
          }
          if (prevOperator === '-') {
            caseResult -= tmp;
          } else {
            caseResult += tmp;
          }
        }
      }
      if (caseResult === 0) result.push(expression);
    });
    result[result.length - 1] += '\n';
  }

  result[result.length - 1] = result[result.length - 1].replace('\n', '');

  return result.join('\n');
}

console.log(main(input));

module.exports = main;
