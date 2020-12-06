function split_array(myArray,index)
{
    return [myArray.slice(0,index), myArray.slice(index)];
    
}
console.log(split_array(['a','b','c','d','e'],3))