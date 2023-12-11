#!/usr/bin/node

const arg = process.argv[2];
// const Print = 'X'

if (!isNaN(arg)) {
    const Size = parseInt(arg);

    for (i = 0; i < Size; i++) {
        console.log('X'.repeat(Size));
    }
} else{
    console.log('Missing size');
}
