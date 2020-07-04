/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-anagrams/problem
    ------------------------
*/

import java.util.Scanner;

public class Solution {

    static final int SIZE = 26; //26 beacuse A to Z 26 letter.
    static boolean isAnagram(String a, String b) {
        int nA = a.length();
        int nB = b.length();
        a = a.toLowerCase();
        b = b.toLowerCase();
        int[] freqA = new int[SIZE];
        int[] freqB = new int[SIZE];
        if(nA == nB){
            for (int i = 0; i < nA; i++){
                freqA[a.charAt(i) - 'a']++;
                freqB[b.charAt(i) - 'a']++;   
            }
            for (int i = 0; i < SIZE; i++){
                if(freqA[i] != freqB[i]){
                    return false;
                }   
            }
            return true;
        }
        else{
            return false;
        }
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
