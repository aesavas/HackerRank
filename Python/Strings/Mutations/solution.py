"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/whats-your-name/problem
"""

# In this problem there are two possible solutions.


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return string = "".join(l)


def mutate_string_alternative(string, position, character):
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    s_new = mutate_string_alternative(s, int(i), c)
    print(s_new)
