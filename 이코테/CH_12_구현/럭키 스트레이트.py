import sys

N = list(map(int, sys.stdin.readline().strip()))
print("LUCKY" if sum(N[:len(N)//2]) == sum(N[len(N)//2:]) else "READY")

