#!/usr/bin/node
const r = require('request');
r(process.argv[2], function (error, response, body) {
  const info = JSON.parse(body);
  let count = 0
  let d = {}
  if (info.length == 0){
    console.log(d)
}
  else{
  let b = info[0]['userId']
    for (let i = 0; i < info.length; i++){
        a = info[i]['userId']
    if (info[i]['userId'] == b){
        if (info[i]['completed'] == true){
        count += 1}
    }
    else {
        if (count != 0){
        d[b] = count}
        if (info[i]['completed'] == true){
            count = 1
        }
        else{
            count = 0
        }
        b = info[i]['userId']
    }
    }
    if (count != 0){
    d[b] = count}
console.log(d)}
});
