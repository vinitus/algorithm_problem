const main = require('./14621_나만 안되는 연애');

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

// makeTestInstance(undefined, undefined);
makeTestInstance(
  `5 7
M W W W M
1 2 12
1 3 10
4 2 5
5 2 5
2 5 10
3 4 3
5 4 7`,
  34
);
makeTestInstance(
  `3 3
M W M
1 2 1 
2 3 1
1 3 1`,
  2
);
makeTestInstance(
  `4 4
M W M W
1 2 1
2 3 1
3 4 1
1 4 2`,
  3
);
