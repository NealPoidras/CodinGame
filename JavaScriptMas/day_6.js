const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});
function reverseAString(word)
{
    return word.split("").reverse();
    
}
