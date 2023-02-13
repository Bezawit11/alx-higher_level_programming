#!/usr/bin/node
const r = require('request');
r(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
