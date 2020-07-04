/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-string-tokens/problem
    ------------------------
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        // We need to delete spaces beginning of the string and end of the string.
        s = s.trim();

        // We have to check if the string only space, we finish the program.
        if(s.length() == 0){
            System.out.println(0);
            System.exit(0);
        }
        String[] wordArray = s.split("[ !,?._'@]+");
        System.out.println(wordArray.length);
        for(int i=0; i<wordArray.length; i++){
            System.out.println(wordArray[i]);
        }
        scan.close();
    }
}

