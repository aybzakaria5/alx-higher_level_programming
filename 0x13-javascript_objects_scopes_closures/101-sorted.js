#!/usr/bin/node

const Dict = require('./101-data').dict;
const dictByOccurrence = {};

for (const keyId in Dict) {
  const valueOccurrence = Dict[keyId];

  if (!dictByOccurrence[valueOccurrence]) {
    dictByOccurrence[valueOccurrence] = [];
  }
  dictByOccurrence[valueOccurrence].push(keyId);
}
console.log(dictByOccurrence);
