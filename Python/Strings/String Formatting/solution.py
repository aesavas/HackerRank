"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


def print_formatted(number):
    space = len(bin(number)[2:])
    for i in range(1, n+1):
        # I started second character because first two digit is useless for this problem.
        octNumber, hexNumber, binNumber = oct(
            i)[2:], hex(i)[2:].upper(), bin(i)[2:]
        # This string formating reference from pyformat.info (You can see details in Padding and aligning strings section.)
        print("{:>{space}} {:>{space}} {:>{space}} {:>{space}}".format(
            i, octNumber, hexNumber, binNumber, space=space))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
