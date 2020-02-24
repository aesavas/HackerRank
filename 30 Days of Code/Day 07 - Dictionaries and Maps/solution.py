"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
"""
from sys import stdin   # We need this module for reading unknown number of input.
if __name__ == "__main__":
    phoneBook = dict()
    number = int(input())
    for i in range(number):
        person = tuple(map(str, input().split()))
        phoneBook[person[0]] = person[1]
    # The problem said that we do no know number of input. So, we read all of inputs.
    names = stdin.read().splitlines()
    for name in names:
        if name in phoneBook:
            print("{}={}".format(name, phoneBook[name]))
        else:
            print("Not found")
