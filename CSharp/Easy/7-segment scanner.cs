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

    public static List<string> createAsciiList()
    {
        List<string> ls = new List<string>(10);
        ls.Add(" _ \n| |\n|_|");//0
        ls.Add("   \n  |\n  |");//1
        ls.Add(" _ \n _|\n|_ ");//2
        ls.Add(" _ \n _|\n _|");//3 etc...
        ls.Add("   \n|_|\n  |");
        ls.Add(" _ \n|_ \n _|");
        ls.Add(" _ \n|_ \n|_|");
        ls.Add(" _ \n  |\n  |");
        ls.Add(" _ \n|_|\n|_|");
        ls.Add(" _ \n|_|\n _|");
        return ls;
    }
    public static List<string> getNumberAscii(string line1,string line2,string line3)
    {   int tmp = 0;
        List<string> ls = new List<string>();
        for(int i = 3 ;i<=line1.Length;i+=3)
        {
            ls.Add(line1[tmp..i]+"\n"+line2[tmp..i]+"\n"+line3[tmp..i]);
            //Console.WriteLine(line1[tmp..i]+"\n"+line2[tmp..i]+"\n"+line3[tmp..i]);
            tmp=i;
        }
        return ls;
    }

    public static string identifyAsciiOne(List<string> ls)
    {
        List<string> ascii = createAsciiList();// Creation de ma liste de nombre en Ascii
        string str = "";
        foreach(string toTest in ls){
            if(ascii.Contains(toTest))
            {
                str+=ascii.IndexOf(toTest).ToString();
            }
        }
        return str;
    }
    static void Main(string[] args)
    {
        string line1 = Console.ReadLine();
        string line2 = Console.ReadLine();
        string line3 = Console.ReadLine();
        List<string> ls = getNumberAscii(line1,line2,line3);
        Console.WriteLine(identifyAsciiOne(ls));
    }
}