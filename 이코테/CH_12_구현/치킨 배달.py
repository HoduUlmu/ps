import itertools
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
chicken_list = []
house_list = []
ans = sys.maxsize

for i in range(N):
    for j, x in enumerate(map(int, read().split())):
        if x == 1:
            house_list.append((i, j))
        elif x == 2:
            chicken_list.append((i, j))

for comb in list(map(list, itertools.combinations(chicken_list, M))):
    dist = []
    for house in house_list:
        min_dist = sys.maxsize
        for c in comb:
            min_dist = min(min_dist, abs(house[0] - c[0]) + abs(house[1] - c[1]))
        dist.append(min_dist)
    ans = min(ans, sum(dist))

print(ans)





