#!/usr/bin/node
let x = 0;
for (x = 0; x < process.argv.length;) { x++; }
if (x === 2) { console.log('No argument'); } else if (x === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
