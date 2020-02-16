"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/nested-list/problem
"""
if __name__ == '__main__':
    students = list()
    # This part to take input for list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # List is sorted according to score.
    students.sort(key=lambda x: x[1])
    lowestScore = students[0][1]
    # This part to find second lowest score.
    for name, score in students:
        if score > lowestScore:
            secondLowestScore = score
            break
    # This filter part to find same score.
    printingList = list(filter(lambda x: x[1] == secondLowestScore, students))
    # Then, I sorted list according to names.
    printingList.sort(key=lambda x: x[0])
    for name, score in printingList:
        print(name)
