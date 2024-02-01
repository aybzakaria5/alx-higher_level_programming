#!/usr/bin/node
// a script that retrivtes the satatu code of a request

const request = require('request');

const url = process.argv[2];
if (process.argv.length !== 3) {
  console.log('Usage:  <./file.js> <url>');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (response) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(error);
  }
});
