#!/usr/bin/node
// a script that reads from a file
const { error } = require('console');
const fs = require('fs');
const pathFile = process.argv[2];

fs.readFile(pathFile, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
