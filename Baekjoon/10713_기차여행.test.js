const main = require('./10713_기차여행');

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
1 3 2 4
120 90 100
110 50 80
250 70 130`,
  550
);
makeTestInstance(
  `8 5
7 5 3 5 4
12 5 8
16 2 1
3 1 5
17 12 17
19 7 5
12 2 19
4 1 3`,
  81
);
// makeTestInstance(undefined, undefined);
