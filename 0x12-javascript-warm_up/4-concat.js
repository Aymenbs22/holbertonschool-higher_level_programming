#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) { console.log(process.argv[2], 'is', process.argv[2]); } else if (process.argv.length === 3) { console.log(process.argv[2], 'is', process.argv[3]); } else { console.log(process.argv[2], 'is', process.argv[3]); }
