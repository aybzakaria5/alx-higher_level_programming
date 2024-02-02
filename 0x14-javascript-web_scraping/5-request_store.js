#!/usr/bin/node
// a script that scrape a url and write its body into a file

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const fileName = process.argv[3];
if (process.argv.length !== 4) {
  console.log('Usage : <./script.js> <url> <filename>');
  process.exit(1);
}
request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, { encoding: 'utf-8', flag: 'w' }, (erro) => {
      if (err) {
        console.error(erro);
      }
    });
  }
});
