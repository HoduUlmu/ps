import sys

read = sys.stdin.readline
while True:
    m, n = map(int, read().split())
    if m == 0 and n == 0:
        break

    parent = list(range(m))
    graph = sorted([tuple(map(int, read().split())) for _ in range(n)], key=lambda x: x[2])
    dist = 0

    def find_parent(node: int):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    for g in graph:
        fp, sp = find_parent(g[0]), find_parent(g[1])
        if fp != sp:
            dist += g[2]
            parent[fp] = parent[sp] = min(fp, sp)

    print(sum([x[2] for x in graph]) - dist)




