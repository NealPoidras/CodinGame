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
    static int definePower(int[] tab)
    {
        Array.Sort(tab);
        int min = int.MaxValue;
        for(int i=1;i<tab.Length;i++)
        {
            if(min>tab[i]-tab[i-1]){min=tab[i]-tab[i-1];}
        }
        return min;
    }
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int[] tab= new int[N];
        for (int i = 0; i < N; i++)
        {
            Console.Write("Choose the power : ");
            int pi = int.Parse(Console.ReadLine());
            Console.WriteLine();
            tab[i] = pi;
        }

        Console.WriteLine("Voici le min : "+definePower(tab));
        Console.ReadLine();
    }
}