using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static public long Calcul(long r1)
    {
        String r1_string = r1.ToString();
        foreach(char str in r1_string){
            r1+= long.Parse(Convert.ToString(str));
        }
        return r1;
    }
    static void Main(string[] args)
    {
        long r1 = long.Parse(Console.ReadLine());
        long r2 = long.Parse(Console.ReadLine());
        while(r1!=r2)
        {
            if(r1<r2){r1 = Calcul(r1);}
            else{r2 = Calcul(r2);}
        }
        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        Console.WriteLine(r1);
    }
}