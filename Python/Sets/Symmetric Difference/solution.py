"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
"""
if __name__ == "__main__":
    counterM = int(input())
    M = set(map(int, input().split()))
    counterN = int(input())
    N = set(map(int, input().split()))
    for i in sorted(M.symmetric_difference(N)):
        print(i)
