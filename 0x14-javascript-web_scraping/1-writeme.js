#!/usr/bin/node
// a script tha write a content into a file

const fs = require('fs');
const filePath = process.argv[2];

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <filePath> <content>');
  process.exit(1); // Exit with an error code
}

fs.writeFile(filePath, process.argv[3], { flag: 'w' }, (err) => {
  if (err) {
    console.error(err);
  }
});
