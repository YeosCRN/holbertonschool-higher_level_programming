#!/usr/bin/node

exports.esrever = function (list) {
  const reserve = [];
  for (let x = list.length - 1; x >= 0; x--) {
    reserve.push(list[x]);
  }
  return reserve;
};
