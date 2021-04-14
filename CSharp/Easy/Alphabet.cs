using System;
using System.Collections;
using System.Collections.Generic;

class Answer 
{
    /// <returns>the character of which s is the​​​​​​‌​​‌​​​​‌​​‌‌‌​​‌​​​​​‌‌‌ representation</returns>
    public static char ScanChar(string s)
    {
        String letter = "?";
        for(char ch = 'A';ch<='Z';ch++)
        {
            if(s == AsciiArt.PrintChar(ch)){letter = ch.ToString();}
        }
        return Convert.ToChar(letter);
    }
}