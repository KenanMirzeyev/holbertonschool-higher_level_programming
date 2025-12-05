#!/usr/bin/node
const x = process.argv[2];
const y = parseInt(x, 10);

if (isNaN(y)) {
	console.log('Missing size');
} else if (y > 0) {
	for (let i = 0; i < y; i++) {
		console.log('X'.repeat(y));
	}
}
