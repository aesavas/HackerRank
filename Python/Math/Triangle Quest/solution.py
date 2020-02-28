"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-quest-1/problem
"""
"""
There is a math trick in this question. I did not know that. If you do not know it, probably you can not do it.
Integers greater than 0 and less than 10:
(10**1)//9 = 1
(10**2)//9 = 11
(10**3)//9 = 111
(10**4)//9 = 1111
(10**5)//9 = 11111
(10**6)//9 = 111111
(10**7)//9 = 1111111
(10**8)//9 = 11111111
(10**9)//9 = 111111111

and if we multiply with for loop counter , we can solve problem.
"""

for i in range(1,int(input())):
    print(i * ((10**i)//9))