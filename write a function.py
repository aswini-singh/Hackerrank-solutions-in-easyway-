#Problem: https://www.hackerrank.com/challenges/py-hello-world/problem

def is_leap(year):

    leap = False

    if (year % 400 == 0) or (year % 4 == 0):
       return True
    if (year %100 == 0):
        return leap
    else:
       return False
    return leap

year=int(input())
print(is_leap(year))