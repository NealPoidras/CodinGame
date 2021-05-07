using System;
using System.Linq;
namespace Palindrome
{
    class Program
    {
        static Boolean isPalindrome(string str1)
        {
            var strReverse = new string(str1.Reverse().ToArray());
            return str1==strReverse;
            
        }
        static void Main(string[] args)
        {
            var palin = Console.ReadLine();
            if(isPalindrome(palin)){Console.WriteLine(palin+" est un palindrome");}
            else{Console.WriteLine(palin+" n'est pas un palindrome");}
            Console.ReadLine();
        }
    }
}

