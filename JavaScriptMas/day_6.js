const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});
function sortByLenght(array){
    return array.sort(function(a,b){
        return a.length-b.length;
    });
}

console.log(sortByLenght(["abc", "", "aaa", "a", "zz"]));
