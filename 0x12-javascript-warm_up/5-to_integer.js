#!/usr/bin/node
if (process.argv[2] === undefined || parseInt(process.argv[2]) === NaN) {
  console.log("Not a number");
} else {
  console.log("My number: " + parseInt(process.argv[2]));
}
