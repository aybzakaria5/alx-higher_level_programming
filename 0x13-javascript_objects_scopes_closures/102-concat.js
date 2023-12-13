#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

const Content1 = fs.readFileSync(argv[2], 'utf8');
const Content2 = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(argv[4], Content1 + Content2);
