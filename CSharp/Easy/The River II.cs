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

    static public int river(int r)
    {
        foreach(char str in Convert.ToString(r))
        {
            r += int.Parse(Convert.ToString(str));
        }
        return r;
    }
    static void Main(string[] args)
    {
        String answer = "NO";
        int r1 = int.Parse(Console.ReadLine());
        for(int i=0;i<=r1;i++)
        {
            int r = river(i);
            if(r==r1){
                answer = "YES";
                break;
                }
        }
        Console.WriteLine(answer);
    }
}