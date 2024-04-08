#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const process = require('process');
if (process.argv.length === 2) {
  console.log(factorial(1));
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
