package Java;
import java.util.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // Number of elements which make up the association table.
        int Q = in.nextInt(); // Number Q of file names to be analyzed.
        HashMap<String,String> myMap = new HashMap<String,String>((int)(N*1.3));
        for (int i = 0; i < N; i++) {
            String EXT = in.next(); // file extension
            String MT = in.next(); // MIME type.
            myMap.put(EXT.toUpperCase(),MT);
        }
        /*for(Map.Entry<String,String> mp:  myMap.entrySet())
        {
            System.err.println("key : "+mp.getKey()+" value : "+mp.getValue());
        }*/
        in.nextLine();
        for (int i = 0; i < Q; i++) {
            String FNAME = in.nextLine(); // One file name per line.
            int lastDotIndex = FNAME.lastIndexOf(".");
            if(lastDotIndex == -1)
            {
                System.out.println("UNKNOWN");
                continue;
            }
            String ext = FNAME.substring(lastDotIndex+1, FNAME.length()).toUpperCase();
            String mineType = myMap.get(ext);
            
            if(mineType==null)
            {
                System.out.println("UNKNOWN");
                continue;
            }
            else
            {
                System.out.println(mineType);
            }
        }
        in.close();

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");


        // For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

    }
}