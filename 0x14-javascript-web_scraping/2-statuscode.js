#!/usr/bin/node
// script that prints the status code of a get request

const request = require('request');
const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log('code:', response.statusCode);
});
