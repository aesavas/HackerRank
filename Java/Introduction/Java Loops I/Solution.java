/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-loops-i/problem
    ------------------------
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        for(int i = 1; i <= 10; i++){
            System.out.println(N + " x " + i + " = " + N*i);
            // We can write it with printf (with using Formatter)
            // System.out.printf("%d x %d = %d%n", N, i, N * i);
            // %d for integers, %n for newline
        }
        scanner.close();
    }
}