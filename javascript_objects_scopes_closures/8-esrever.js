#!/usr/bin/node

exports.esrever = function (list) {
  let reserve = []
  let y = 0;
  for (let x = list.length - 1; x >= 0; x--) {
    reserve.push(list[x]);
  }
  return reserve;
};
