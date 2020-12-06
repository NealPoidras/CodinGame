const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});
function reverseAString(word)
{
    return word.split("").reverse();
    
}

rl.question("Choose the word to  reverse : ",answer=>{
    console.log(reverseAString(answer));
    rl.close();
});