"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-nested-logic/problem
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def calculateFine(r, e):
    """
        r = returnedDate
        e = expectedDate
    """

    if r.year == e.year:
        if r.month == e.month:
            if r.day == e.day: return 0
            else: return abs(r.day - e.day) * 15
        else:
            if r.month < e.month: return 0
            else : return abs(r.month - e.month) * 500
    else:
        if r.year < e.year: return 0
        else: return 10000


if __name__ == "__main__":
    date = list(map(int, input().split()))
    returnDate = Date(date[0], date[1], date[2])
    date = list(map(int, input().split()))
    expectedDate = Date(date[0], date[1], date[2])
    print(calculateFine(returnDate,expectedDate))