#!/usr/bin/node

const [, , arg] = process.argv;
const num = parseInt(arg, 10);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
