#!/usr/bin/node
const imparray = require('./100-data.js').list;
let i = 0;
const map = imparray.map(l => l * i++);
console.log(imparray);
console.log(map);
