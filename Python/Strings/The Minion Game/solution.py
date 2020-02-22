"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/the-minion-game/problem
"""
"""
The logic is finding number of substring which starts with vowels and consonants.
For example: BANANA
First letter is B. Now, find substring which starts with B.
B,BA,BAN,BANA,BANAN,BANANA ==> 6 substring.
Purpose of (len(string) - i) is to find number of substring which starts with current letter.
"""


def minion_game(string):
    kevinScore = 0
    stuartScore = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevinScore += (len(string)-i)
        else:
            stuartScore += (len(string)-i)

    if kevinScore > stuartScore:
        print("Kevin {}".format(kevinScore))
    elif kevinScore < stuartScore:
        print("Stuart {}".format(stuartScore))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
