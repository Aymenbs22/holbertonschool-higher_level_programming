#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let c = 0; c < x; c++) {
    console.log('X'.repeat(x));
  }
}
