/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
function calculNumber(number)
{
   numbers =String(number).split("")
   numbers.forEach(element=>
   {
       number = number + parseInt(element)
       
   })
   return number
}

let r1 = parseInt(readline());
let r2 = parseInt(readline());

while(r1!=r2){
   if(r1<r2){r1 = calculNumber(r1)}
   else{calculNumber(r2 = calculNumber(r2))}
}
// Write an answer using console.log()
// To debug: console.error('Debug messages...');

console.log(r1);
