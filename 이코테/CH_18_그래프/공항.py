import sys


def find_parent(parent: list, node: int):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_node(parent: list, a: int, b: int):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


read = sys.stdin.readline
g, p = int(read()), int(read())
parents = [x for x in range(g + 1)]
ans = 0

for i in range(p):
    spot = find_parent(parents, int(read()))
    if spot == 0:
        break
    union_node(parents, spot, spot - 1)
    ans += 1

print(ans)

