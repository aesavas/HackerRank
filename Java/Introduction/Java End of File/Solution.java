/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-end-of-file/problem
    ------------------------
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = 1;
        while(scan.hasNext()){
            System.out.println(n + " " +scan.nextLine());
            n++;
        }
        scan.close();
    }
}
