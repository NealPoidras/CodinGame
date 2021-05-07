using System;

namespace Factorial
{
    class Program
    {

        static public int factorial_recursive(int n)
        {
            if(n==1){return 1;}
            else {return n*factorial_recursive(n-1);}
        }
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("in recursive way :"+factorial_recursive(n));
            int var = 1;
            for(int i=1;i<=n;i++)
            {
                var=var*i;
            }
            Console.WriteLine("in loop way:"+var);

        }
    }
}
