/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-bitwise-and/problem
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    public static int bitwiseAnd(int n, int k){
        int A = 1;
        int maxValue = 0;
        while(A <= n-1){
            int B = A + 1;
            while(B <= n){
                if((A&B) < k && maxValue < (A&B)) maxValue = A&B;
                B++;
            }
            A++;
        }

        return maxValue;

    }



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String[] nk = scanner.nextLine().split(" ");

            int n = Integer.parseInt(nk[0]);

            int k = Integer.parseInt(nk[1]);
            System.out.println(bitwiseAnd(n,k));
        }

        scanner.close();
    }
}
