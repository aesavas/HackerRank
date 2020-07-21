"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

    I used simple 6k ± 1 method for these problem.
    src : https://en.wikipedia.org/wiki/Primality_test
"""

def isPrime(number):
    if number == 1:
        return "Not prime"
    elif number <= 3:
        return "Prime"
    elif (number%2 == 0 or number%3==0):
        return "Not prime"
    i = 5
    while i*i <=number:
        print(i)
        if number%i ==0 or number%(i+2)==0:
            return "Not prime"
        i = i + 6
        print(i)

    return "Prime"

if __name__ == '__main__':
 
    for _ in range(int(input())):
        print(isPrime(int(input())))