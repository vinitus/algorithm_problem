const main = require('./3020_개똥벌레');

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
  `6 7
  1
  5
  3
  3
  5
  1`,
  '2 3'
);
makeTestInstance(
  `14 5
    1
3
4
2
2
4
3
4
3
3
3
2
3
3`,
  '7 2'
);
makeTestInstance(
  `6 5
5
0
0
0
0
0`,
  '1 5'
);
makeTestInstance(
  `6 5
1
0
1
0
1
0`,
  '0 4'
);
makeTestInstance(
  `10 6
5
1
4
2
3
3
2
4
1
5`,
  '5 6'
);
