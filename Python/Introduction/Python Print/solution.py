"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-print/problem
"""
if __name__ == '__main__':
    n = int(input())
    number = ""
    # n+1 -> Because in range function, n+1 is not in the range.
    for i in range(1, n+1):
        number += str(i)
    print(number)
