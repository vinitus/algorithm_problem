const main = require('./7511_소셜네트워킹어플리케이션');

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
  `2
3
1
0 1
2
0 1
1 2
5
3
0 1
1 2
3 4
2
0 2
1 3`,
  `Scenario 1:
1
0

Scenario 2:
1
0`
);
// makeTestInstance(undefined, undefined);
