#!/usr/bin/node
//AAAAAAAAA

const args = process.argv.slice(2).map(Number);


if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const filtered = args.filter(n => n !== max);

  if (filtered.length === 0) {
    console.log(0);
  } else {
    const second = Math.max(...filtered);
    console.log(second);
  }
