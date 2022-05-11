import sys

read = sys.stdin.readline
n = int(read())
student_list = [read().split() for _ in range(n)]
student_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in student_list:
    print(student[0])