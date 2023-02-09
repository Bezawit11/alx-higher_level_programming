#!/usr/bin/node
const response = await fetch(process.argv[2]);
console.log('code: ', response.status);
