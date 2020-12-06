function depositProfit(deposit,rate,threshold)
{
    let cpt =1;
    while(deposit<threshold)
    {
        deposit +=(rate/100)*deposit;
        cpt++;
    }
    return cpt;
}

console.log(depositProfit(120,20,170));