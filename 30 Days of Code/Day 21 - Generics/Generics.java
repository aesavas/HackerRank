/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-generics/problem
------------------------------------------------------------------------
    Fewer languages are enabled for this challenge. Thus, I used Java.

*/

import java.util.*;

class Printer <T> {
    public static <T> void printArray(T[] inputArray ){
        for(int i=0; i<inputArray.length; i++){
            System.out.println(inputArray[i]);
        }
    }
}

public class Generics {
    
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        scanner.close();
        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if(Printer.class.getDeclaredMethods().length > 1){
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    } 
}