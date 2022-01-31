import collections
import sys

graph = collections.defaultdict(list)


def input():
    read = sys.stdin.readline
    int(read())
    e = int(read())
    for _ in range(e):
        c1, c2 = map(int, read().split())
        graph[c1] += [c2]
        graph[c2] += [c1]


def virus(node, visited):
    visited.append(node)
    for adj in graph[node]:
        if adj not in visited:
            virus(adj, visited)
    return len(visited) - 1


if __name__ == '__main__':
    input()
    print(virus(1, []))
