"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-arrays/problem
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(" ".join(str(i) for i in arr[::-1]))
