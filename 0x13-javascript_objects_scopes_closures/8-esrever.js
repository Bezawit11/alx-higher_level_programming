#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    l[j] = list[i];
    j++;
  }
  return l;
};
