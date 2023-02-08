#!/usr/bin/node
const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
