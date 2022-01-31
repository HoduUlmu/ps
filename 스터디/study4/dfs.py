from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# dfs 재귀호출
def dfs_recursive(node, visited):
    # 호출 시 파라미터로 넘어온 node는 방문 처리
    visited.append(node)

    # 파라미터로 넘어온 노드의 인접 노드를 모두 가져와 visited 배열에 없으면 재귀 호출
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    # 업데이트 된 visited 리턴
    return visited


# dfs 스택 방식
def dfs_stack(start):
    # 방문한 노드를 담을 빈 리스트와 시작점을 담은 스택 선언
    visited = []
    stack = [start]

    # 스택에 노드가 있는 동안
    while stack:
        print(stack)
        # 스택에서 팝하여 노드를 가져옴
        top = stack.pop()

        # 가져온 노드가 방문한 노드가 아니라면 visited에 넣어준다
        # 그 후 인접 노드를 모두 stack에 append
        if top not in visited:
            visited.append(top)
            for adj in graph[top]:
                stack.append(adj)

    # visited 리턴
    return visited


# 큐를 활용한 bfs
def bfs_queue(start):
    # 시작 노드를 담은 visited 리스트와 데크를 선언
    visited = [start]
    q = deque([start])

    # 큐에 값이 있을 동안
    while q:
        # 큐에서 노드를 가져와 인접 노드를 찾는다
        # visited에 인접 노드가 없다면 추가시켜주고 큐에 삽입
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)
    # visited 리턴
    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]
assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]
