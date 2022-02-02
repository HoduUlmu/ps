import sys

read = sys.stdin.readline
n = int(read())
members = []

for i in range(n):
    member_info = read().split()
    member_age = int(member_info[0])
    member_name = member_info[1]
    members.append((i, member_age, member_name))

members = sorted(members, key=lambda x: (x[1], x[0]))

for member in members:
    print(member[1], member[2])
