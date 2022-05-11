import bisect
import sys

read = sys.stdin.readline
n, c = map(int, read().split())
houses = sorted([int(read()) for _ in range(n)])

start = houses[1] - houses[0]
end = houses[-1] - houses[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    v = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= v + mid:
            v = houses[i]
            count += 1
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)