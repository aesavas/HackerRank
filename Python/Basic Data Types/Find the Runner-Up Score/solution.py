"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
if __name__ == '__main__':
    n = int(input())
    # I converted to list because I wanted to use sort() function.
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in arr:
        if (i < arr[0]):
            print(i)
            break
