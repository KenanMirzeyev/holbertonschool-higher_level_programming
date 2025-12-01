#!/usr/bin/node
const a = process.argv[2];
const n = parseInt(a);

if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number:', n);
}
