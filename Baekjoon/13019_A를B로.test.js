const main = require('./13019_A를B로');

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
  `ABC
CBA`,
  2
);
makeTestInstance(
  `A
B`,
  -1
);
makeTestInstance(
  `AAABBB
BBBAAA`,
  3
);
makeTestInstance(
  `A
A`,
  0
);
makeTestInstance(
  `DCABA
DACBA`,
  2
);
// makeTestInstance(undefined, undefined);
