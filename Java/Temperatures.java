package Java;
import java.util.*;
import java.math.*;
class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt();
        if (N == 0)
            System.out.println("0");
        else {
            int T;
            int min = Integer.MAX_VALUE;
            for (int i = 0; i < N; i++) {
                T = in.nextInt();
                if (Math.abs(T) < Math.abs(min) || (T == -min && T > 0))
                    min = T;
            }
            System.out.println(min);
        }
        in.close();
    }
}
    

