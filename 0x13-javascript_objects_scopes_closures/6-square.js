#!/usr/bin/node
const Parent = require('./5-square');

class Square extends Parent {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += ch;
      }
      console.log(shape);
    }
  }
}

module.exports = Square;
