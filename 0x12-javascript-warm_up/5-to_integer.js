#!/usr/bin/node

const process = require('process');

if (parseInt(process.argv[2])) {
  console.log(parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
