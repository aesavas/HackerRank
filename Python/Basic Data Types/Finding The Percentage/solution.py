"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    calculateAverageList = student_marks[query_name]
    average = format(float(sum(calculateAverageList))/3, '.2f')
    print(average)
