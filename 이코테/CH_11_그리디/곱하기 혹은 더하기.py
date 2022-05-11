import sys

s = list(map(int, sys.stdin.readline().strip()))
ans = 0

for c in s:
    if ans <= 1 or c <= 1:
        ans += c
    else:
        ans *= c
print(ans)


