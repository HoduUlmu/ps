import collections
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
ball_list = list(map(int, read().split()))
counter = collections.Counter(ball_list)

length = len(ball_list)
ans = (length * (length - 1)) / 2

count = [v for v in counter.values() if v > 1]
for c in count:
    ans -= (count[1] * (count[1] - 1)) / 2

print(int(ans))
