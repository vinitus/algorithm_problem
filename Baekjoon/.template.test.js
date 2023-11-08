const main = require('./.template');

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

test(`${testCaseString} ${makeTestCaseNum.next().value}`, () => {
  expect(main()).toBe(undefined);
});

test(`${testCaseString} ${makeTestCaseNum.next().value}`, () => {
  expect(main()).toBe(undefined);
});
