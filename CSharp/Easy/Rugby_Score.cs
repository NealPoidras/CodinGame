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
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int i = 0;
        int j = 0;
        int k = 0;
        while(i*5<=N)
        {
            j=0;
            while(j<=i && i*5+j*2<=N)
            {
                k=0;
                while(i*5+j*2+k*3<=N)
                {
                    if(i*5+j*2+k*3==N)
                    {
                        Console.WriteLine(i+" "+j+" "+k);
                    }
                    k+=1;
                }
                j+=1;
            }
            i+=1;
        }
    }
}