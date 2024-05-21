#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error reading file:', error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
}
);
