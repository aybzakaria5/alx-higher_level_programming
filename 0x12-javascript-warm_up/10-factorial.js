#!/usr/bin/node
const arg = process.argv[2]

function fct (num) {
    if (num === 0) {
        return 1;
    }
    return num * fct((num - 1))
}

if (!isNaN(arg)) {
    const num = parseInt(arg)
    console.log(fct(num))
} else {
    console.log(fct(0))
}