"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-mod-divmod/problem
"""
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print("{}\n{}\n{}".format(a//b, a % b, divmod(a, b)))
