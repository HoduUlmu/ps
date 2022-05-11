import sys

read = sys.stdin.readline

N = int(read())
fear_list = sorted(list(map(int, read().split())))

group_num = 0
member_num = 0

for fear in fear_list:
    member_num += 1
    if member_num >= fear:
        group_num += 1
        member_num = 0

print(group_num)
