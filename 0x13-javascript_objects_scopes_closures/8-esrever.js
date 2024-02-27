#!/usr/bin/node
exports.esrever = function (list) {
  let r = list.length - 1;
  let l = 0;
  while ((r - l) > 0) {
    const tmp = list[r];
    list[r] = list[l];
    list[l] = tmp;
    l++;
    r--;
  }
  return list;
};
