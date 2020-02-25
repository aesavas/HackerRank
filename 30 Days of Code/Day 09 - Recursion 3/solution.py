"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-recursion/problem
"""

# If you use this solution in Hackerrank solution, just copy the function. Because main part is different from website.


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
