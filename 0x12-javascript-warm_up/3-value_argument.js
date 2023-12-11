#!/usr/bin/node

const argv = process.argv;

if (argv === undefined) {
    console.log('No argument');
} else {
    console.log(argv[2]);
}
