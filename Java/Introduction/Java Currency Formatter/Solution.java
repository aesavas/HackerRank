/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-currency-formatter/problem
    ------------------------
*/

import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        // We need to create locale for India. Because there is no built-in Locale.
        Locale localeForIndia = new Locale("en", "IN");
        
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String india = NumberFormat.getCurrencyInstance(localeForIndia).format(payment);
        String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

        
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}