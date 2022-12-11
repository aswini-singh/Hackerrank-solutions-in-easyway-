#Problem: https://www.hackerrank.com/challenges/py-hello-world/problem


n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])


