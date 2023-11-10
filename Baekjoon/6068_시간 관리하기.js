const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [N, ...inputStr] = input.split('\n');
  const [lastToDo, ...scheduleArr] = inputStr
    .map((inputLine) => inputLine.split(' ').map(Number))
    .sort((a, b) => {
      return b[1] - a[1];
    });

  let time = scheduleArr.reduce((prev, [t, s]) => {
    if (s <= prev) prev = s - t;
    else prev -= t;

    return prev;
  }, lastToDo[1]);

  if (time < 0) return -1;

  return time;
}

console.log(main(input));

module.exports = main;
