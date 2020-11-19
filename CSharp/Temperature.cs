using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
namespace CSharp
{
    class Temperature
    {

        public static int ComputeClosestToZero(int[] ts)
        {
            int min = int.MaxValue;
            if(ts.Length==0){return 0;}
            foreach(int t in ts)
            {
                if(Math.Abs(t)< Math.Abs(min) || (t == -min && t>0)){min = t;}
            }
            return min;
        }

        static void Main(string[] args)
        {
            string[] inputs;
            int n = int.Parse(Console.ReadLine());
            int[] ts = new int[n];
            inputs = Console.ReadLine().Split(' ');
            for (int i = 0; i < n; i++)
            {
                ts[i] = int.Parse(inputs[i]);
            }
            var stdtoutWriter = Console.Out;
            Console.SetOut(Console.Error);
            int solution = ComputeClosestToZero(ts);
            Console.SetOut(stdtoutWriter);
            Console.WriteLine(solution);
        }
        
    }
}
