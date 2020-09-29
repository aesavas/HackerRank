/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-string-reverse/problem
    ------------------------
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    
    public static int calculateSumOfHourglass(int[][] arr){
        int max=-64; // Because max can be minimum -63 (-9X7) so sometimes we can give negative numbers.
        for(int i=0; i<(arr.length - 2); i++){
            for(int j=0; j<arr[i].length-2; j++){
                int sum =0;
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2];//top
                sum = sum + arr[i+1][j+1];                  //middle
                sum = sum + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];//bottom

                if(sum > max) max = sum;
            }
        }
        return max;
    }


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }
        System.out.println(calculateSumOfHourglass(arr));

        scanner.close();
    }
}
