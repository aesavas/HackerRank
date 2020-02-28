"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-power-mod-power/problem
"""
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    print("{}\n{}".format(pow(a, b), pow(a, b, m)))
