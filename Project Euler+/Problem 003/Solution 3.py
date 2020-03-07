"""
author : Ali Emre SAVAS
Link : https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
"""


def findLargestPrimeFactor(number):
    factor = 2
    while(factor <= int(number ** 0.5)):
        if(number % factor == 0):
            number /= factor
        else:
            factor += 1
    return int(number)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(findLargestPrimeFactor(n))
