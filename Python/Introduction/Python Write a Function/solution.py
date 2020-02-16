"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/write-a-function/problem
"""


def is_leap(year):
    leap = False

    if(year >= 1900 and year <= 10**5):
        if(year % 4 == 0):
            if(year % 100 == 0):
                if(year % 400 == 0):
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

    return leap


year = int(input())
print(is_leap(year))
