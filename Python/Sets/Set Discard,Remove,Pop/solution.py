"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/forum
"""
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    operation = input().split()
    if operation[0].lower() == "discard":
        s.discard(int(operation[1]))
    elif operation[0].lower() == "remove":
        s.remove(int(operation[1]))
    elif operation[0].lower() == "pop":
        s.pop()
    else:
        print("Wrong operation!")
print(sum(s))
