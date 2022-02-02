import sys

read = sys.stdin.readline
n = int(read())
nums = set()

for _ in range(n):
    nums.add(int(read()))

nums = sorted(nums)
print(*nums, sep='\n')