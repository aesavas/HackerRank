"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
from cmath import phase
if __name__ == "__main__":
    z = input()
    print(abs(complex(z)))
    print(phase(complex(z)))
