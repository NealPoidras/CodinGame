using System;
using System.Collections.Generic;

namespace Anagram
{
    class Program
    {
        static Boolean isAnagram(string str1,string str2)
        {
            var str1R = str1.ToLower().ToArray();
            var str2R = str2.ToLower().ToArray();
            Array.Sort(str1R);
            Array.Sort(str2R);
            return new string(str1R) == new string(str2R);
        }
    static void subString(String s){
        Dictionary<string, int> map= new Dictionary<string, int>();
  
        for(int i = 0; i < s.Length; i++){
            for(int j = i; j < s.Length; j++){
                char[] valC = s.Substring(i, j+1-i).ToCharArray();
                Array.Sort(valC);
                string val = new string(valC);
                if (map.ContainsKey(val)) 
                    map[val]=map[val]+1;
                else
                    map.Add(val, 1);
            }
        }
        Console.Write(map.Values);
    }
        static void Main(string[] args)
        {
            Console.WriteLine(isAnagram("Nezl","enaL"));
            Console.WriteLine(subString("ABC"));
            Console.ReadLine();
        }
    }
}
