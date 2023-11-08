const main = require('./.template');

function* counter() {
  let cnt = 1;
  while (cnt <= 100) {
    yield cnt++;
  }
}

test(`번호: 문제이름 case ${counter().next().value}`, () => {
  expect(main()).toBe(undefined);
});
