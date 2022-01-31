import sys

read = sys.stdin.readline
n, m = map(int, read().split())
cards = sorted(list(map(int, read().split())))

result = 0
length = len(cards)

cnt = 0
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_val = cards[i] + cards[j] + cards[k]
            if sum_val <= m:
                result = max(result, sum_val)

print(result)