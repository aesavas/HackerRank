"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""
if __name__ == '__main__':
    n = int(input())
    number = bin(n)[2:]
    counter, result = 0, 0
    for i in range(len(number)):
        if number[i] == '1':
            counter += 1
            result = max(result, counter)
        else:
            counter = 0
    print(result)
