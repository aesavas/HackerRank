"""
author : Ali Emre SAVAS
Link : https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""
def sumOfSequence(x):
    return x*(x+1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        n -= 1  # Because problem says below n
        # We substracts multiplies of 15 because they exist two times in the sequence
        # Also, we use bitwise right-shift for division. Because hackerrank does not accept /2. Some test cases' inputs contain very large numbers.
        print(int(3*sumOfSequence(n//3) + 5 *
                  sumOfSequence(n//5) - 15*sumOfSequence(n//15)) >> 1)
