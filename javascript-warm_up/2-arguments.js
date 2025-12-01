#!/usr/bin/node
const acount = process.argv.length - 2;

if (acount === 0) {
	console.log('No argument');
} else if (acount === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
