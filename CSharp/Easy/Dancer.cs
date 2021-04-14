using System;
using System.Collections.Generic;

namespace Easy
{
    class Program
    {
        public static int getPositionAt(int n){
            List<int> ls = new List<int>();
            ls.AddRange(new List<int>{0,1,-1,-4,-5,3});
            return ls[n%6];
        }
        static void Main(string[] args)
        {
            Console.WriteLine(getPositionAt(Int32.Parse(Console.Read("Select the Position of the dancer you want to know : "))));
        }
    }
}
