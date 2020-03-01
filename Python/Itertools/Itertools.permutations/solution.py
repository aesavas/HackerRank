"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/itertools-permutations/problem
"""

from itertools import permutations

if __name__ == "__main__":
    S, k = input().split()
    permutationList = sorted(list(permutations(S, int(k))))
    for i in permutationList:
        print("".join(i))
