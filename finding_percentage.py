n=int(input())
student_marks={}
for i in range(n):
    name, *line = input().split()
    scores=list(map(float,line))
    stdent_marks[name]=scores
query_name = input()
output=list(student_marks[query_name])
per = sum(output)/len(output)
print("%.2f" %per)
