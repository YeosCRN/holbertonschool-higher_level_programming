#!/usr/bin/node

const SquarePrime = require('./5-square.js');

class Square extends SquarePrime {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let x = 0; x < this.width; x++) { row += c; }
    for (let x = 0; x < this.height; x++) { console.log(row); }
  }
}

module.exports = Square;
