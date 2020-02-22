"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/capitalize/problem
"""


# If you want to use in Hackerrank, just copy the function. Main section is different in Hackerrank.
def solve(s):
    name = s.split(" ")
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    return " ".join(name)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
