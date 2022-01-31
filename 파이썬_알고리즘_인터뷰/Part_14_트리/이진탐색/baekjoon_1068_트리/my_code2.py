import collections
import sys

read = sys.stdin.readline
n = int(read())
child_info = collections.defaultdict(list)
parent_info = list(map(int, read().split()))
remove_node = int(read())
stack = [remove_node]

for idx, p in enumerate(parent_info):
    if idx == remove_node:
        continue
    child_info[p].append(idx)

while stack:
    node = stack.pop()

    if child_info[node]:
        for child in child_info[node]:
            stack.append(child)

    child_info[node] = [-1]

leaf = len([i for i in range(n) if not child_info[i]])
print(leaf)
