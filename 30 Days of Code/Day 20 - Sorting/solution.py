"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-sorting/problem
"""

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
           a[j], a[j+1]  = a[j+1], a[j]
           numberOfSwaps += 1
           totalSwaps += 1
    
    if numberOfSwaps == 0: break


print("Array is sorted in {} swaps.".format(totalSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))