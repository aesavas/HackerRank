/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-string-compare/problem
    ------------------------
*/



import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        smallest = s.substring(0, k);
        largest = s.substring(0, k);
        for(int i=1; i <= s.length()-k; i++){
            String temp = s.substring(i, i+k);
        
            if(temp.compareTo(smallest) < 0) smallest = temp;
            
            if(temp.compareTo(largest) > 0) largest = temp;
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}