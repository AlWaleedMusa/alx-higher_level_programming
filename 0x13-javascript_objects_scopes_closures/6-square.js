#!/usr/bin/node
const Square = require('./5-square.js');

class square extends Square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char);
      }
      console.log();
    }
  }
}
module.exports = square;
