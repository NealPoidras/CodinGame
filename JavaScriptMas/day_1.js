function findNumberOfCandies(candies,numberOfChildren)
{
    return Math.floor(candies/numberOfChildren)*numberOfChildren;
}

console.log(findNumberOfCandies(10,3))