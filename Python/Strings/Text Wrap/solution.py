"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/text-wrap/problem
"""


def wrap(string, max_width):
    newString = ""
    for i in range(0, len(string), max_width):
        newString += string[i:(i+max_width)] + "\n"  # \n for new line.
    # newString = newString[:(len(newString)-1)] If you do not want to print last blank line, you can add this line for this.
    return newString


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
