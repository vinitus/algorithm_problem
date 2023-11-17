const fs = require('fs');
const { exec } = require('child_process');
const filename = process.argv[2];

fs.readFile('./Baekjoon/.template.js', 'utf-8', (err, data) => {
  if (err) throw err;
  fs.promises.writeFile('./tmp/' + filename + '.js', data).then(() => {
    openFile(`${filename}.js`);
  });
});

fs.readFile('./Baekjoon/.template.test.js', 'utf-8', (err, data) => {
  if (err) throw err;
  const transformedData = updateRequireTarget(data, filename);
  fs.promises.writeFile('./tmp/' + filename + '.test.js', transformedData).then(() => {
    openFile(`${filename}.test.js`);
  });
});

function updateRequireTarget(originalFile, filename) {
  const dataArr = originalFile.split('\n');
  dataArr[0] = `const main = require("./${filename}");\r`;
  return dataArr.join('\n');
}

function openFile(filename) {
  exec(`code ./tmp/${filename}`, (err, stdout, stderr) => {
    if (err) {
      console.warn(err);
      return;
    }

    if (stderr) {
      console.error(stderr);
      return;
    }

    console.log(`${filename} is created successfully.`);
  });
}
