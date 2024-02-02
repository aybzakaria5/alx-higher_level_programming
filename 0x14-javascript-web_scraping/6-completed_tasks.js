#!/usr/bin/node
// scraping from an api completed tasks
const request = require('request');
const url = process.argv[2];
// const fs = require("fs");
if (process.argv.length !== 3) {
  console.log('Usage: <./file.js> <url>');
  process.exit(1);
}
request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const onlyCompleted = {};
    body.forEach(todoTask => {
      if (!(todoTask.userId in onlyCompleted) && todoTask.completed) {
        onlyCompleted[todoTask.userId] = 1;
      } else if (todoTask.completed) {
        onlyCompleted[todoTask.userId]++;
      }
    });
    console.log(onlyCompleted);
  }
});
