const main = require('./1600_말이되고픈원숭이');

function* makeTestCaseNumGenerator() {
  let cnt = 1;
  while (cnt <= 100) {
    yield cnt++;
  }
}

const makeTestCaseNum = makeTestCaseNumGenerator();

function getTestCaseString() {
  const fileDirArr = __filename.split('\\');
  const fileFullname = fileDirArr[fileDirArr.length - 1];
  const filename = fileFullname.split('.test.js')[0];
  const [problemNum, problemName] = filename.split('_');

  return `${problemNum}: ${problemName} case`;
}

const testCaseString = getTestCaseString();

const makeTestInstance = (idx, result) => {
  return test(`${testCaseString} ${makeTestCaseNum.next().value}`, () => {
    expect(main(idx)).toBe(result);
  });
};

makeTestInstance(
  `1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0`,
  4
);
makeTestInstance(
  `2
5 2
0 0 1 1 0
0 0 1 1 0`,
  -1
);
