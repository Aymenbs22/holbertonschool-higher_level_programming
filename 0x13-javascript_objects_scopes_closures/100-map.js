#!/usr/bin/node
var imparray = require('./100-data.js').list;
var i = 0;
const map = imparray.map(l => l * i++);
console.log(imparray);
console.log(map);
