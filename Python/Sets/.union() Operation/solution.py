"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-set-union/problem
"""
if __name__ == "__main__":
    numberOfSetA = int(input())
    setA = set(map(int, input().split()))
    numberOfSetB = int(input())
    setB = set(map(int, input().split()))
    print(len(setA.union(setB)))
