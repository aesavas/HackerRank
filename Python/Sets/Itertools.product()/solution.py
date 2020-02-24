"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/itertools-product/problem
"""
from itertools import product

if __name__ == "__main__":
    setA = list(map(int, input().split()))
    setB = list(map(int, input().split()))
    # We change i as a string because join() method does not accept tuple.
    print(" ".join(str(i) for i in list(product(setA, setB))))
