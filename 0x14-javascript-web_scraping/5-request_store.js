#!/usr/bin/node
const fs = require('fs');
const r = require('request');
r(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const b = response.body;
  fs.writeFile(process.argv[3], b, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
