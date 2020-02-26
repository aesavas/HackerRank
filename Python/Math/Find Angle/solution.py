"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/find-angle/problem
"""
"""
It comes from triangle median formula. We have ABC right trianle, also we have MB median. It means that AM, MC and MB edges are equal.
So, we can solve this problem with inverse of tan.
"""

import math
if __name__ == "__main__":
    AB = int(input())
    AC = int(input())
    print(str(round(math.degrees(math.atan2(AB, AC)))) + "°")
