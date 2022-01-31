import sys

read = sys.stdin.readline
n, m = map(int, read().split())
cards = sorted(list(map(int, read().split())))

ans = -1
min_diff = sys.maxsize
left = 0

while left < len(cards) - 2:

    val = cards[left] + cards[left + 1] + cards[left + 2]

    if val > m:
        break

    diff = m - val
    if diff < min_diff:
        min_diff = diff
        ans = val
        if diff == 0:
            break
    left += 1

print(ans)