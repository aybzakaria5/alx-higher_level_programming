#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);

  data.characters.forEach(item => {
    request(item, (err, resp, bdy) => {
      if (err) {
        console.error(err);
        return;
      }
      const dt = JSON.parse(bdy);
      console.log(dt.name);
    });
  });
});
