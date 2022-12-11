#Problem: https://www.hackerrank.com/challenges/py-hello-world/problem

n = int(input())
if n % 2 != 0 :
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")