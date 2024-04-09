#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDic = {};

Object.getOwnPropertyNames(dict).forEach(obj => {
  if (newDic[dict[obj]] === undefined) {
    newDic[dict[obj]] = [obj];
  } else {
    newDic[dict[obj]].push(obj);
  }
});
console.log(newDic);
