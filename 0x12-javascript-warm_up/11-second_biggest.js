#!/usr/bin/node
function second_biggest(arr){
const b = []
for (let i = 2; i < arr.length; i++){
b[i - 2] = arr[i];
}
b.sort()
b.reverse()
return b[1]
}

if (isNaN(parseInt(process.argv[2]))){
  console.log("0")
}
else{
console.log(second_biggest(parseInt(process.argv)))
}
