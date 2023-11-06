const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (!input) return;

  const [n, first, ...remainedInput] = input.split('\n');
  const [start, end] = first.split(' ').map(Number);

  // 경우가 1개인 경우에 대한 전처리
  if (n === '1') return end - start + 1;

  // 365일까지의 배열 생성
  const schedule = Array(366).fill(0);

  // 첫번째 입력에 대한 전처리
  forStatement(start, end, (idx) => (schedule[idx] = 1));

  // 첫번째 입력을 제외한 나머지 처리
  remainedInput.forEach((item) => {
    const [s, e] = item.split(' ').map(Number);
    forStatement(s, e, (idx) => (schedule[idx] += 1));
  });

  let depth = 0; // 일정이 중첩된 깊이를 나타내는 변수
  let continuity = 0; // 연속된 일정을 나타내는 변수
  let result = 0;

  schedule.forEach((item) => {
    if (!item) {
      if (depth && continuity) {
        result += depth * continuity;
        depth = 0;
        continuity = 0;
      }
    } else {
      if (depth < item) {
        depth = item;
      }
      continuity += 1;
    }
  });

  if (depth && continuity) result += depth * continuity;

  return result;
}

// 여러개의 for문 만들기를 편하게 해주는 도구
function forStatement(s, e, fn) {
  for (let idx = s; idx <= e; idx += 1) {
    fn(idx);
  }
}

console.log(main(input));

module.exports = main;
