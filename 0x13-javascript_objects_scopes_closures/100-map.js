#!/usr/bin/node
const li = require('./100-data.js').list;
const newli = li.map((num, idx) => num * idx);
console.log(li);
console.log(newli);
