#!/usr/bin/node
const axios = require('axios');

async function makeRequest () {
  const config = {
    method: 'head',
    url: process.argv[2]
  };

  const res = await axios(config);

  console.log('code: ', res.status);
}
makeRequest();
