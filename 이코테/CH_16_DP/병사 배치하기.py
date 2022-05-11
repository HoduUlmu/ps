import sys

read = sys.stdin.readline

n = int(read())
soldiers = list(map(int, read().split()))
max_len = [1] * n
for i in range(len(soldiers)):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            max_len[i] = max(max_len[i], max_len[j] + 1)

print(len(soldiers) - max(max_len))