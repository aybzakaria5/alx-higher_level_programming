#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class suqare extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = suqare;
