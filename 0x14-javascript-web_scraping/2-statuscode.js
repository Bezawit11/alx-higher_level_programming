#!/usr/bin/node
const r = require('request');
r(process.argv[2], function (response, body) {
  console.log('code:', response && response.statusCode);
});
