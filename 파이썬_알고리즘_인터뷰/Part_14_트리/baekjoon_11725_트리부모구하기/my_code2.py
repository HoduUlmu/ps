import collections
import sys

read = sys.stdin.readline
n = int(read())
graph_info = collections.defaultdict(list)
parent_list = [0] * (n - 1)

for _ in range(n - 1):
    node1, node2 = map(int, read().split())
    graph_info[node1].append(node2)
    graph_info[node2].append(node1)


stack = [1]

while stack:
    cur = stack.pop()
    for node in graph_info[cur]:
        # 자바에서는 안될듯
        if node == parent_list[cur - 2]:
            continue
        parent_list[node - 2] = cur
        stack.append(node)

for v in parent_list:
    print(v)