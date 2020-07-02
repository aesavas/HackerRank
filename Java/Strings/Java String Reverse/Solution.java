/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-string-reverse/problem
    ------------------------

    There are two way to reverse string.
    First, we need some knowledge about StringBuilder
    Second, it is primitive (simple) way to reverse string.
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        sc.close();
       
        /*
        First way
        ------------------------------------------
        StringBuilder builder = new StringBuilder();
        builder.append(A);
        String reverse = builder.reverse().toString();*/

        /*Second way
        ------------------------------------------- */
        String reverse = "";
        for(int i = A.length()-1 ; i >= 0; i--){
            reverse += A.charAt(i);
        }


        if(A.compareTo(reverse) == 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }

        
    }
}



