const main = require('./2230_수고르기');

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
  `3 3
1
5
3`,
  4
);
// makeTestInstance(undefined, undefined);
