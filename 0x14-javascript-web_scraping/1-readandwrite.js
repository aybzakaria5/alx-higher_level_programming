#!/usr/bin/node
// a script tha write a content into a file

const fs = require('fs');
// const filePath = process.argv[2];

// if (process.argv.length !== 4) {
//   console.error('Usage: node script.js <filePath> <content>');
//   process.exit(1); // Exit with an error code
// }

fs.writeFile("filePath", process.argv[2], { flag: 'w' }, (err) => {
  if (err) {
    console.error(err);
  }
});
console.log("now we are reading from the file :")
fs.readFile("filePath", "utf-8", (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data)
} )