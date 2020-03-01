"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""
from itertools import combinations_with_replacement

if __name__ == "__main__":
    S, k = input().split()
    # We need to sort binary list in the list. So, I use like this "sorted(combinations_with_replacement(S, int(k)))[j])"
    combinationList = [sorted(sorted(combinations_with_replacement(S, int(k)))[
                              j]) for j in range(len(sorted(combinations_with_replacement(S, int(k)))))]
    for i in sorted(combinationList):
        print("".join(i))
