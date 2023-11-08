const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string') return;

  const inputArr = input.split('\n');
}

console.log(main(input));

module.exports = main;
