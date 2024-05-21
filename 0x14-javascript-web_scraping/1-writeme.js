#!/usr/bin/node
// Write a string to a file

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath) {
    console.error('Please provide a file path as the first argument.');
    process.exit(1);
    }

fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error('Error writing to file:', err);
        }
    });
