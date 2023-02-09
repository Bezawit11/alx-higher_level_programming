#!/usr/bin/node
const r = require('request');
r(process.argv[2], function (error, response, body) {
  const info = JSON.parse(body);
  let count = 0
  for (let a in info['results']){
      for (i in a){
        console.log(i)
        for (let j in i['characters']){
          console.log(j)
              if (j == "https://swapi-api.alx-tools.com/api/people/18/"){
                  count += 1}}}}
  console.log(count)
});
