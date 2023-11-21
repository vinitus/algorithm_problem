const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();

function main(input) {
  if (typeof input !== 'string' || !input) return;

  const [T, ...inputArr] = input.split('\n');
  let totalResult = [];

  let totalIdx = 0;
  for (let t = 0; t < T; t += 1) {
    const n = Number(inputArr[totalIdx++]);
    const k = Number(inputArr[totalIdx++]);
    const visited = Array.from({ length: n }, (_, k) => k);

    inputArr
      .slice(totalIdx, totalIdx + k)
      .map((tmp) => tmp.split(' ').map(Number))
      .forEach(([s, e]) => {
        if (find(visited, s) !== find(visited, e)) union(visited, s, e);
      });

    totalIdx += k;
    const m = Number(inputArr[totalIdx++]);
    const testcaseResult = inputArr
      .slice(totalIdx, totalIdx + m)
      .map((line) => line.split(' ').map(Number))
      .reduce((prevResult, [s, e]) => {
        if (find(visited, s) !== find(visited, e)) prevResult.push(0);
        else prevResult.push(1);
        return prevResult;
      }, []);
    totalIdx += m;

    totalResult.push(`Scenario ${t + 1}:\n` + testcaseResult.join('\n'));
  }

  return totalResult.join('\n\n');
}

function find(arr, idx) {
  if (arr[idx] !== idx) arr[idx] = find(arr, arr[idx]);
  return arr[idx];
}

function union(arr, s, e) {
  const newS = find(arr, s);
  const newE = find(arr, e);
  if (newS < newE) arr[newE] = newS;
  else arr[newS] = newE;
}

console.log(main(input));

module.exports = main;
