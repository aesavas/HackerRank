"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""


def numberOfCaptainRoom(K, listOfRoomNumber):
    # We do not want to access last element of list because if we access it, function will has 'out of index' exception.
    for i in range(0, len(listOfRoomNumber) - 1, K):
        if(listOfRoomNumber[i] != listOfRoomNumber[i+1]):
            return listOfRoomNumber[i]
    # If we does not find in for loop, it has to be last element of list.
    return listOfRoomNumber[-1]


if __name__ == "__main__":
    K = int(input())
    listOfRoomNumber = list(map(int, input().split()))
    listOfRoomNumber.sort()
    print(numberOfCaptainRoom(K, listOfRoomNumber))
