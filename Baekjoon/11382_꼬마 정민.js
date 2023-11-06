const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

function main(input) {
  let [a, b, c] = input[0].split(' ').map((item) => parseInt(item, 10));

  return a + b + c;
}

console.log(main(input));

module.exports = main;
