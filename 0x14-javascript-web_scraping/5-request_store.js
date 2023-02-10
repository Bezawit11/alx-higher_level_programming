#!/usr/bin/node
const fs = require('fs');
const r = require('request');
r(process.argv[2], function (error, response, body) {
fs.writeFile(JSON.parse(body), process.argv[3], (err) => {
if (err) throw err;
});
});
