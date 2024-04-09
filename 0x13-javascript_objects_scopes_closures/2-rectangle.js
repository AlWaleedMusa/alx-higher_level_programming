#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
s = new Rectangle(-1, 3)
