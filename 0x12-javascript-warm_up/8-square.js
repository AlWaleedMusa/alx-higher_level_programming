#!/user/bin/node
const process = require('process');
if (parseInt(process.argv[2])) {
  const len = parseInt(process.argv[2]);
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
