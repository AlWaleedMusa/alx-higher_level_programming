#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    counter += (list[i] === searchElement) ? 1 : 0;
  }
  return counter;
};
