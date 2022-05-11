# 시간초과
import sys

read = sys.stdin.readline
n = int(read())
cards = [int(read()) for _ in range(n)]
ans = 0

while len(cards) > 2:
    ans += cards.pop() + cards.pop()
    cards.append(ans)

print(ans + cards[0] + cards[1])
