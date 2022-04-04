#!/usr/bin/node
const integer = process.argv[2];
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
