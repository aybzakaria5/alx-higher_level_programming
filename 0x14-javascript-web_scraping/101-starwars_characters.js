#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  printItems(characters, 0);
});

function printItems (items, index) {
  request(items[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < items.length) {
        printItems(items, index + 1);
      }
    }
  });
}
