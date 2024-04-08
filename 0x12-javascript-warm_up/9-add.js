#!/usr/bin/node
function add(a, b) {
    return a + b
}
process = require('process')
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])))
