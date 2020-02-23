"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/no-idea/problem
"""

# The important idea is we have to search on set not on list. (For time complexity.)
if __name__ == "__main__":
    n, m = map(int, input().split())
    numberList = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    happiness = len([i for i in numberList if i in setA]) - len([i for i in numberList if i in setB])
    print(happiness)
