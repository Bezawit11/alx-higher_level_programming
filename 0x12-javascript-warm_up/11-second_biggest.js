#!/usr/bin/node
function SecondBiggest (arr) {
  const b = [];
  for (let i = 2; i < arr.length; i++) {
    b[i - 2] = parseInt(arr[i]);
  }
  b.sort();
  b.reverse();
  return b[1];
}

if (isNaN(parseInt(process.argv[2])) || isNaN(parseInt(process.argv[3]))) {
  console.log(0);
} else {
  console.log(SecondBiggest(process.argv));
}
