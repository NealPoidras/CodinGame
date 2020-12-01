package Java.Easy;
import java.util.*;
public class Chuck_Norris {

    public static void main(String args[]) 
    {
        Scanner in = new Scanner(System.in);
        String message = in.nextLine();
        
        byte[] bytes = message.getBytes();
        String converted = "";
        
        for (int i = 0; i < message.length(); i++)
        {
            String temp = Integer.toBinaryString(bytes[i]);
            while (temp.length() < 7)
                temp = "0" + temp;
            converted += temp;
        }
            
        int i = 0;
    	char currentChar;
    	while (i < converted.length()) 
    	{
    		if (converted.charAt(i) == '0') 
    		{
    			System.out.print("00 ");
    			currentChar = '0';
    		}
    		else 
    		{
    			System.out.print("0 ");
    			currentChar = '1';
    		}
    		
    		while (converted.charAt(i) == currentChar) 
    		{
    			System.out.print("0");
    			i++;
    			if(i == converted.length()) 
    			    break;
    		}
    		
    		if (i < converted.length())
    		    System.out.print(" ");
		}  
		in.close();  
    }
}
