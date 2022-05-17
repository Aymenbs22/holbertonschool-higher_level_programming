#!/usr/bin/node
const axios = require('axios');
const id = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    console.log(response.data.results[id - 1].title);
  })
  .catch(function (error) {
    console.log(error);
  });
