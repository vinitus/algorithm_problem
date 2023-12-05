const main = require('./14719_빗물');

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
  `4 4
3 0 1 4`,
  5
);
makeTestInstance(
  `4 8
3 1 2 3 4 1 1 2`,
  5
);
makeTestInstance(
  `3 5
0 0 0 2 0`,
  0
);
// makeTestInstance(undefined, undefined);
