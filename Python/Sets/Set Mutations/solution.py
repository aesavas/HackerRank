"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-set-mutations/problem
"""
if __name__ == "__main__":
    numberOfSetA = int(input())
    setA = set(map(int, input().split()))
    numberOfOperation = int(input())
    for i in range(numberOfOperation):
        operation, numberOfItem = input().split()
        tempSet = set(map(int, input().split()))
        # input gives as directly method name. So, we can use in eval() method.
        eval("setA."+operation.lower()+"(tempSet)")
        # I newly learn eval() method and I like it so much :D
    print(sum(setA))
