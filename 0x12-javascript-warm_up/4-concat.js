#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

console.log(`${arg1 ? arg1 : 'undefined'} is ${arg2 ? arg2 : 'undefined'}`);
