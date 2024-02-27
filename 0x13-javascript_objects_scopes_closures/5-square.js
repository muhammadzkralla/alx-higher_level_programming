#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (len) {
    super(len, len);
  }
}

module.exports = Square;
