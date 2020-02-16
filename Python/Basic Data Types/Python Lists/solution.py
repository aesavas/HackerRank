"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/python-lists/problem
"""
if __name__ == '__main__':
    N = int(input())
    listOfNumbers = list()
    for _ in range(N):
        process = list(map(str, input().split()))
        process_type = process[0].lower()
        if(process_type == "append"):
            listOfNumbers.append(int(process[1]))
        elif(process_type == "insert"):
            listOfNumbers.insert(int(process[1]), int(process[2]))
        elif(process_type == "remove"):
            if(int(process[1]) in listOfNumbers):
                listOfNumbers.remove(int(process[1]))
        elif(process_type == "sort"):
            listOfNumbers.sort()
        elif(process_type == "pop"):
            listOfNumbers.pop()
        elif(process_type == "reverse"):
            listOfNumbers.reverse()
        elif(process_type == "print"):
            print(listOfNumbers)
