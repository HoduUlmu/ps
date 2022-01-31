import collections
import sys

read = sys.stdin.readline
n = int(read())

parent_info = collections.defaultdict(list)

for _ in range(n - 1):
    node1, node2 = map(int, read().split())
    parent_info[node1].append(node2)
    parent_info[node2].append(node1)

sorted(parent_info.items())


print(sorted(parent_info.items()))