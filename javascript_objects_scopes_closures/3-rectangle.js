#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let x = 0; x < this.width; x++) { row += 'X'; }
    for (let x = 0; x < this.height; x++) { console.log(row); }
  }
}

module.exports = Rectangle;
