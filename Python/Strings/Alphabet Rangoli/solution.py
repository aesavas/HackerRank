"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""
import string


def print_rangoli(size):
    # This blank for
    alphabet = tuple(" "+string.ascii_lowercase)
    lineSize = n * 4 - 3
    # UPPER SECTION
    for i in range(size, 0, -1):
        row = "-".join(alphabet[size:i:-1] + alphabet[i:size+1])
        print(row.center(lineSize, "-"))
    # BOTTOM SECTION
    for i in range(2, size+1):
        row = "-".join(alphabet[size:i:-1] + alphabet[i:size+1])
        print(row.center(lineSize, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
