#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    console.log(
      ('X'.repeat(this.width) + '\n').repeat(this.height - 1) +
        'X'.repeat(this.width)
    );
  }
}

module.exports = Rectangle;
