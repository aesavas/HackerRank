"""
author : Ali Emre SAVAS
Link : https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""


def sumOfFibonacci(maxRange):
    # nextValue gives us the next term of sequence
    firstValue, secondValue, nextValue = 0, 1, 0
    sumOfEven = 0
    while(nextValue <= maxRange):
        if nextValue % 2 == 0:
            sumOfEven += nextValue
        firstValue, secondValue = secondValue, nextValue
        nextValue = firstValue + secondValue
    return sumOfEven


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sumOfFibonacci(n))
