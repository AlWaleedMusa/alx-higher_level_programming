#!/usr/bin/node
const process = require('process');
if (process.argv) {
  const var1 = process.argv[2];
  const var2 = process.argv[3];
  console.log(`${var1} is ${var2}`);
}
