# 시간 초과
import sys

read = sys.stdin.readline
n = int(read())
members = []

for _ in range(n):
    members.append(tuple(read().split()))
members = sorted(members, key=lambda x: (int(x[0]), members.index(x)))
# members.sort(key=lambda x: (members.index(x)))

for member in members:
    print(member[0], member[1])
