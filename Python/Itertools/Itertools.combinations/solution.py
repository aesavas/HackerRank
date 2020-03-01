"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/itertools-combinations/problem
"""
from itertools import combinations

if __name__ == "__main__":
    S, k = input().split()
    for i in range(1, int(k)+1):
        combinationList = [sorted(sorted(combinations(S, i))[j])
                           for j in range(len(sorted(combinations(S, i))))]
        for k in sorted(combinationList):
            print("".join(k))
