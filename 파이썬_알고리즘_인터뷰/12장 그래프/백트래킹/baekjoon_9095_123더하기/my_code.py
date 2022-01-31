import sys


def solve(n):
    ans = 0

    def dfs(num):
        nonlocal ans
        if num >= n:
            if num == n:
                ans += 1
            return False

        for i in range(1, 4):
            if dfs(num + i) is False:
                break

    dfs(0)
    return ans


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    case = int(input())
    print(solve(case))
