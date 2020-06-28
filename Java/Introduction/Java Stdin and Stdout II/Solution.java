/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-stdin-stdout/
    ------------------------
*/


import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();  // dummy input because of \n
        String s = scan.nextLine();
        scan.close();
        
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}