#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += 'X';
    }
    for (let l = 0; l < this.height; l++) {
      console.log(x);
    }
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
