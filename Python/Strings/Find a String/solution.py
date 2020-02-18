"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/find-a-string/problem
"""

# This solution is much easier understand than other.
"""
def count_substring(string, sub_string):
    numberOfSubstring = 0 # It counts number of substring inside of string.
    for i in range(0, len(string)-len(sub_string)+1): # Because I can traverse no more than the substring length. 
        if(string[i] == sub_string[0]):
            numberOfSameChar = 1 # It counts number of same character substring and string. It starts 1 because it is checked inside of "if"
            i += 1
            for j in range(1, len(sub_string)):
                if(string[i] == sub_string[j]):
                    i += 1
                    numberOfSameChar += 1
                else:
                    break
            if(numberOfSameChar == len(sub_string)):
                numberOfSubstring += 1
    return numberOfSubstring
"""


def count_substring(string, sub_string):
    numberOfSubstring = 0  # It counts number of substring inside of string.
    # Because I can traverse no more than the substring length.
    for i in range(0, len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string):
            numberOfSubstring += 1
    return numberOfSubstring


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
