#!/usr/bin/node
// script that prints the number of movies where “Wedge Antilles” is acting.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error reading file:', error);
  }
  const films = JSON.parse(body).results;
  console.log(films.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
}
);
