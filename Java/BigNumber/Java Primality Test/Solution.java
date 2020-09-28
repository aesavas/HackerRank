/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-primality-test/problem
    ------------------------
*/


import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] game) {
        // Return true if you can win the game; otherwise, return false.
        return isSolvable(leap, game, 0);
    }

    public static boolean isSolvable(int leap, int[] game, int i){
        if(i >= game.length) return true;
        if(i < 0 || game[i] == 1) return false; //if i is minus this means return to much or if game[i] is 1 it means location visited before.

        game[i] = 1; // if no true or false it means you can visit the location.

        return isSolvable(leap, game, i + 1) || //It means go a step forward
        isSolvable(leap, game, i - 1) || //It means go back one step
        isSolvable(leap, game, i + leap); // It means go a leap forward.

    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}