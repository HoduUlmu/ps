import bisect
import sys

read = sys.stdin.readline

n = int(read())
soldiers = list(map(int, read().split()))
lis = [-soldiers[0]]

for soldier in soldiers:
    p = bisect.bisect_left(lis, -soldier)
    if p >= len(lis):
        lis.append(-soldier)
    else:
        lis[p] = -soldier

print(len(soldiers) - len(lis))
