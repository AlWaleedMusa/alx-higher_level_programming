#!/usr/bin/node
// script that prints the number of movies where “Wedge Antilles” is acting.

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/";

request.get(url, function (error, response, body) {
    if (error) {
        console.error('Error reading file:', error);
    }
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
        for (const character of film.characters) {
        if (character.includes('/18/')) {
            count++;
        }
        }
    }
    console.log(count);
    }
);