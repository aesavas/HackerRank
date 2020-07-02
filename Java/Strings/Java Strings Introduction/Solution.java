/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-strings-introduction/problem
    ------------------------
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        sc.close();
        
        int length = A.length() + B.length();
        System.out.println(length);
        if(A.compareTo(B) > 0 ){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        String capitalizeA = A.substring(0, 1).toUpperCase()+A.substring(1);
        String capitalizeB = B.substring(0, 1).toUpperCase()+B.substring(1);
        System.out.println(capitalizeA + " " + capitalizeB);

        
    }
}
