"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-loops/problem
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n*i))
