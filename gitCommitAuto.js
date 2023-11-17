const fs = require('fs');
const { exec } = require('child_process');

fs.readdir('./tmp', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    throw err;
  }

  // data에 들어있는 JavaScript 파일 할당
  const [algorithmFilename, testFilename] = data;

  // 지금 디렉토리인 tmp에 해당하는 filePath 생성
  const algorithmFilePath = `./tmp/${algorithmFilename}`;
  const testfilePath = `./tmp/${testFilename}`;

  // 백준 디렉토리 filePath 생성
  const newAlgorithmFilePath = `./Baekjoon/${algorithmFilename}`;
  const newTestfilePath = `./Baekjoon/${testFilename}`;

  // 커밋 메시지를 위한 문제 번호
  const problemNumber = algorithmFilename.split('_')[0];

  // promise를 통한 순서보장 및 백준 디렉토리로 파일 복사
  const algorithmFilePromise = fs.promises.copyFile(algorithmFilePath, newAlgorithmFilePath);
  const testFilePromise = fs.promises.copyFile(testfilePath, newTestfilePath);

  // 두 파일 복사가 끝난 다음을 위한 Promise.all
  Promise.all([algorithmFilePromise, testFilePromise])
    .then(() => {
      // 복사된 파일에 대한 git add 처리
      exec(`git add ${newAlgorithmFilePath}`, (err, stdout, stderr) => {
        execCallback({ filename: newAlgorithmFilePath, err, stdout, stderr });
      });

      exec(`git add ${newTestfilePath}`, (err, stdout, stderr) => {
        execCallback({ filename: newAlgorithmFilePath, err, stdout, stderr });
      });

      // tmp에 들어있는 파일 삭제
      fs.unlink(algorithmFilePath, (err) => {
        execCallback({ err });
      });

      fs.unlink(testfilePath, (err) => {
        execCallback({ err });
      });
    })
    .then(() => {
      // git commit 처리, 커밋 메시지는 문제번호임
      exec(`git commit -m "${problemNumber}"`, (err, stdout, stderr) => {
        execCallback({ err, stdout, stderr });
      });
    });
});

function execCallback({ err, stdout, stderr, filename }) {
  if (err) {
    console.error(err);
    throw err;
  }

  if (stderr) {
    console.error(stderr);
    throw stderr;
  }

  if (stdout) {
    console.log(stdout);
    return;
  }

  if (filename) {
    console.log(`success: git add ${filename}`);
  }
}
