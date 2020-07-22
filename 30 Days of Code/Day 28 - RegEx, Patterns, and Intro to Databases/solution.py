"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-regex-patterns/problem
"""

import re

if __name__ == '__main__':
    N = int(input())
    names = list()
    regexName = "[a-z]"
    regexEmail = "[a-z]{1,}@gmail.com"
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if(re.search(regexName, firstName) and len(firstName)<20):
            if (re.search(regexEmail, emailID) and len(emailID)<50):
                names.append(firstName)
    names.sort()
    for name in names:
        print(name)
