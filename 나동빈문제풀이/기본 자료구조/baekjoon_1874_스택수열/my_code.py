# 리팩 필요
import sys

read = sys.stdin.readline
n = int(read())
seq = []

is_ok = False
m = 0
stack = []
ans = []
for _ in range(n):
    seq.append(int(read()))

for num in seq:
    if not stack:
        m += 1
        ans.append('+')
        stack.append(m)

    while m <= n:
        if num == stack[-1]:
            stack.pop()
            ans.append('-')
            is_ok = True
            break
        m += 1
        ans.append('+')
        stack.append(m)

    if is_ok:
        is_ok = False
    else:
        ans = ['NO']
        break

for a in ans:
    print(a)


