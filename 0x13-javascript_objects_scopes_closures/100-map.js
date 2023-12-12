#!/usr/bin/node

const List = require('./100-data').list;
const newList = List.map((val, idx) => val * idx);
console.log(List);
console.log(newList);
