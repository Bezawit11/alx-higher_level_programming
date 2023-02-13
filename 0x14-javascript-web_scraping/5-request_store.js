#!/usr/bin/node
const fs = require('fs');
const r = require('request');
r(process.argv[2], function (error, response, body) {
  b = response.body;
  fs.writeFile(process.argv[3], b, 'utf-8', (err) => {
  });
});
