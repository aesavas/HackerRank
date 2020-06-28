/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-loops/problem
    ------------------------

    I do not want to use Math.pow() function. Thus, I try to solve with for loop.
*/

import java.util.*;

public class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for(int j=0; j<n;j++){
                int temp = b; 
                for(int k=0; k<j; k++){
                    temp *= 2; 
                }
                a += temp; // I kept the sum in "a" variable.
                System.out.print(a + " ");
            }
            System.out.println();
        }
        in.close();
    }
}