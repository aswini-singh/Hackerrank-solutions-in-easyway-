#Solution – Set.symmetric_difference() Operation in Python

a = int(input())
set_a = set(map(int ,input().split()))

b = int(input())
set_b = set(map(int , input().split()))

print(len(set_a.symmetric_difference(set_b)))