"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/py-set-add/problem
"""
if __name__ == "__main__":
    counter = int(input())
    countries = set()
    for _ in range(counter):
        countries.add(input())
    print(len(countries))
