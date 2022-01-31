import collections
import sys


def input():
    read = sys.stdin.readline
    n = int(read())
    e = int(read())
    graph = collections.defaultdict(list)
    for _ in range(e):
        c1, c2 = map(int, read().split())
        graph[c1] += [c2]
        graph[c2] += [c1]
    return graph


def virus(graph):
    visited = []
    stack = [1]

    while stack:
        top = stack.pop()

        if top not in visited:
            visited.append(top)
            for adj in graph[top]:
                stack.append(adj)

    print(len(visited) - 1)

# # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
#     while stack:
#         # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
#         top = stack.pop()
#         visited.append(top)
#         # 인접 노드를 방문한다.
#         for adj in graph[top]:
#             if adj not in visited:
#                 stack.append(adj)

if __name__ == '__main__':
    g = input()
    virus(g)
