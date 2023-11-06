const main = require('./20207_달력');

test('20207: 달력 case 1', () => {
  expect(main('1\n2 4\n')).toBe(3);
});

test('20207: 달력 case 2', () => {
  expect(main('7\n2 4\n4 5\n5 6\n5 7\n7 9\n11 12\n12 12\n')).toBe(28);
});

test('20207: 달력 case 3', () => {
  expect(main('5\n1 9\n8 9\n4 6\n3 4\n2 5\n')).toBe(36);
});
