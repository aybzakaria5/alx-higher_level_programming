#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Suqare extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Suqare;
