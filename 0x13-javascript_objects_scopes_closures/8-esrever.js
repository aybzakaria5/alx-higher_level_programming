#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const mid = Math.floor(len / 2);

  for (let i = 0; i < mid; i++) {
    const tmp = list[i];
    list[i] = list[len - 1 - i];
    list[len - 1 - i] = tmp;
  }
  return list;
};
// we can use the unshift() methode => it adds the elemnt at the
// begining of the new list
// or using the push() methode => it adds the element at the end
