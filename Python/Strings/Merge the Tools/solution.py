"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/merge-the-tools/editorial
"""
from collections import OrderedDict


def merge_the_tools(string, k):
    subsequents = [string[i:i+k] for i in range(0, len(string), k)]
    for subset in subsequents:
        print("{}".format("".join(OrderedDict.fromkeys(subset))))
        # print("{}".format("".join(set(subset)))) #If we do not care about order, we can use this line.


# If you do not want to use any modul you can use this function
def merge_the_tools_without_modul(string, k):
    subsequents = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(subsequents)):
        subset = ""
        for letter in subsequents[i]:
            if letter not in subset:
                subset += letter
        print(subset)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    print("")
    merge_the_tools_without_modul(string, k)
