const fs = require('fs');
const filename = process.argv[2];

fs.readFile('./Baekjoon/.template.js', 'utf-8', (err, data) => {
  if (err) throw err;
  fs.writeFile('./' + filename + '.js', data, (err) => {
    if (err) throw err;
  });
});

fs.readFile('./Baekjoon/.template.test.js', 'utf-8', (err, data) => {
  if (err) throw err;
  const transformedData = updateRequireTarget(data, filename);
  fs.writeFile('./' + filename + '.test.js', transformedData, (err) => {
    if (err) throw err;
  });
});

function updateRequireTarget(originalFile, filename) {
  const dataArr = originalFile.split('\n');
  dataArr[0] = `const main = require("./${filename}");\r`;
  return dataArr.join('\n');
}
