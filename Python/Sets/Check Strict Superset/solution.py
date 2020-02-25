"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""
if __name__ == "__main__":
    setA = set(map(int, input().split()))
    n = int(input())
    numberOfSubset = 0
    for _ in range(n):
        tempSet = set(map(int, input().split()))
        if (tempSet.issubset(setA)):
            # If numberOfSubset is equal number of other sets, setA will be superset all of these sets.
            numberOfSubset += 1
    print("{}".format(True if numberOfSubset == n else False))
