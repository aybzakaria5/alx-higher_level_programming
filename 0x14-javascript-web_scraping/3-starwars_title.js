#!/usr/bin/node
// a script that uses an api to scrap some data from it
const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
if (process.argv.length !== 3) {
  console.log('Usage: <./file.js> <filmeId>');
  process.exit(1);
}

request.get(url, (err, res, body) => {
  if (res) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log(err);
  }
});
