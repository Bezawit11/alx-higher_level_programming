#!/usr/bin/node
function factorial(a){
    if (a == 1){
        return 1;
    }
    return a * factorial(a -1)
}
if (isNaN(parseInt(process.argv[2]))){
  console.log("1")
}
else{
 factorial(parseInt(process.argv[2]))
}
