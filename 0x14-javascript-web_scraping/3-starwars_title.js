#!/usr/bin/node
// script that prints the title of a Star Wars movie according to a giving int.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, function (error, response, body) {
    if (error) {
        console.error('Error reading file:', error);
    }
    console.log(JSON.parse(body).title);
});
