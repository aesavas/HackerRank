"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-check-subset/problem
"""
if __name__ == "__main__":
    for _ in range(int(input())):
        numberOfA = int(input())
        setA = set(map(int, input().split()))
        numberOfA = int(input())
        setB = set(map(int, input().split()))
        print(setA.issubset(setB))
