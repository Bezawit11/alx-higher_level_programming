#!/usr/bin/node
const fs = require('fs');
const r = require('request');
r(process.argv[2], function (error, response, body) {
b = response['body'];
console.log(b);
fs.writeFile(str(b), process.argv[3], 'utf-8', (err) => {
if (err) throw err;
});
});
