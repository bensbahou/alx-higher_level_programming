#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint(c) {
    c ||= 'X';
    console.log((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
