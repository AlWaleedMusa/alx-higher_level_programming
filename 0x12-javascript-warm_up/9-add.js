#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const process = require('process');
console.log(add(process.argv[2], process.argv[3]));
