#!/usr/bin/node
// Read the content of a file and print it to the standard output

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log(data);
  }
});
