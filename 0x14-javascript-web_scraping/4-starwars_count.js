#!/usr/bin/node
// a script that uses the request module
// and gets inforamtion from api
// getting in how many movies a person acted
// using the api
// const request = require('request');
const url = process.argv[2];
// const actor = 'https://swapi-api.alx-tools.com/api/people/10/';
// request(url, { json: true }, (err, res, body) => {
//   if (err) {
//     console.log(err);
//   } else {
//     //   const count = body.split('/people/18/');
//     const films = body.results;
//     const match = films.filter((film) => film.characters.includes(actor));
//     const count = match.length;
//     console.log(count);
//   }
// });
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(body.split('/people/18/').length - 1);
});
