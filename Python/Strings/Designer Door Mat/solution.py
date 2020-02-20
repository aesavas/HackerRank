"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/designer-door-mat/problem
"""
nm = input().split()
n, m = int(nm[0]), int(nm[1])
figure = ".|."
# TOP SECTION
for i in range(n//2):
    print((figure*i).rjust((m//2)-1, "-") +
          figure+(figure*i).ljust((m//2)-1, "-"))

# WELCOME SECTION
print("WELCOME".center(m, "-"))

# BOTTOM SECTION
for i in range((n//2), 0, -1):
    print((figure*(i-1)).rjust((m//2)-1, "-") +
          figure+(figure*(i-1)).ljust((m//2)-1, "-"))
