#!/usr/bin/node
const fs = require('fs');
const axios = require('axios');
axios.get(process.argv[2])
  .then(function (response) {
    fs.appendFile(process.argv[3], response.data, (err) => {
      if (err) throw err;
    });
  });
