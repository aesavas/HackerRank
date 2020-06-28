/*
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/java-int-to-string/problem
    -------------------------
    There are 3 ways that I know to convert int to string. You can use any of them.
*/

String s = "";
if(n >= -100 && n <= 100){
    s = String.valueOf(n);
    s = Integer.toString(n);
    s += n;
}

