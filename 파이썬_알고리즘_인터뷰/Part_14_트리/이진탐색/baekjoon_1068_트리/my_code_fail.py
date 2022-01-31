# 노드를 제거했을 때 제거한 노드의 부모 노드가 leaf 노드가 되어버리는 상황을 생각을 안함
import collections
import sys

read = sys.stdin.readline
n = int(read())
child_info = collections.defaultdict(list)
parent_info = list(map(int, read().split()))
remove_node = int(read())
stack = [remove_node]

for idx, p in enumerate(parent_info):
    child_info[p].append(idx)

leaf = [i for i in range(n) if not child_info[i]]

while stack:
    node = stack.pop()

    if node in leaf:
        leaf.remove(node)

    if child_info[node]:
        for child in child_info[node]:
            stack.append(child)


print(len(leaf))