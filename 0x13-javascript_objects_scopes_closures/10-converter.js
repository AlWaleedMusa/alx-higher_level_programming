#!/usr/bin/node
exports.converter = function (base) {
  return (n) => {
    console.log(n.toString(base));
  };
};
