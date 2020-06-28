/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-if-else/problem
    ------------------------
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        if(n % 2 == 1){
            System.out.println("Weird");
        }
        else{
            if(n % 2 == 0 && n >= 6 && N <= 20){
                System.out.println("Weird");
            }
            else{
                System.out.println("Not Weird");
            }
        }
    }
}