#!/usr/bin/node
const r = require('request');
r(process.argv[2], function (error, response, body) {
  const info = JSON.parse(body);
  let count = 0
  for (let i = 0; i < info['results'].length; i++){
    for (let j = 0; j < info['results'][i]['characters'].length; j++){
       a = info['results'][i]['characters'][j];
       if (a == "https://swapi-api.alx-tools.com/api/people/18/")
         {
        count += 1
        }
}
}
  console.log(count)
});
