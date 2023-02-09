#!/usr/bin/node
const r = require('request');
r('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  console.log('code:', response && response.statusCode);
  const info = JSON.parse(body);
  console.log(info['title'])
});
