"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-review-loop/problem
"""

if __name__ == '__main__':
    S = list()
    N = int(input())
    for _ in range(N):
        s = input()
        S.append(s)

    # This solution is classical way
    for i in S:
        odd, even = "", ""  # because we have to reset every step
        for j in range(len(i)):
            if(j % 2 == 0):
                even += i[j]
            else:
                odd += i[j]
        print("{} {}".format(even, odd))

    # This solution with list comprehensions
    for i in S:
        even = [i[j] for j in range(len(i)) if(j % 2 == 0)]
        odd = [i[j] for j in range(len(i)) if(j % 2 == 1)]
        print("{} {}".format("".join(even), "".join(odd)))
