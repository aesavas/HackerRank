"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-operators/problem
"""


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100) #Calculate tip
    tax = meal_cost * (tax_percent / 100) #Calculate tax
    totalCost = meal_cost + tip + tax #Calculate total cost of product
    print(round(totalCost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
