import collections
import heapq


def dijkstra(g: dict, n, start: int, first_dest: int = 0, second_dest: int = 0) -> list:
    heap = [(0, start)]
    dist = [-1] * (n + 1)
    while heap:
        time, node = heapq.heappop(heap)

        if dist[node] == -1:
            dist[node] = time
            if dist[first_dest] != -1 and dist[second_dest] != -1:
                return dist
            for v, w in g[node]:
                new_w = time + w
                heapq.heappush(heap, (new_w, v))

    return dist


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    for x, y, z in fares:
        graph[x].append((y, z))
        graph[y].append((x, z))

    start_dist = dijkstra(graph, n, s)
    min_price = start_dist[a] + start_dist[b]

    for i in range(1, n + 1):
        if i == s:
            continue
        dist = dijkstra(graph, n, i, a, b)
        min_price = min(min_price, start_dist[i] + dist[a] + dist[b]) if dist[a] != -1 and dist[b] != -1 else min_price
    return min_price


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])

# 정확성  테스트
# 테스트 1 〉	통과 (0.12ms, 10.4MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.25ms, 10.2MB)
# 테스트 5 〉	통과 (0.40ms, 10.2MB)
# 테스트 6 〉	통과 (0.28ms, 10.4MB)
# 테스트 7 〉	통과 (0.25ms, 10.4MB)
# 테스트 8 〉	통과 (0.31ms, 10.4MB)
# 테스트 9 〉	통과 (0.69ms, 10.2MB)
# 테스트 10 〉	통과 (0.90ms, 10.5MB)
# 효율성  테스트
# 테스트 1 〉	통과 (14.86ms, 10.3MB)
# 테스트 2 〉	통과 (156.44ms, 10.9MB)
# 테스트 3 〉	통과 (30.67ms, 10.4MB)
# 테스트 4 〉	통과 (24.98ms, 10.3MB)
# 테스트 5 〉	통과 (45.07ms, 10.2MB)
# 테스트 6 〉	통과 (52.59ms, 10.2MB)
# 테스트 7 〉	통과 (1744.42ms, 19.7MB)
# 테스트 8 〉	통과 (2113.61ms, 19.6MB)
# 테스트 9 〉	통과 (1748.55ms, 19.6MB)
# 테스트 10 〉	통과 (1576.72ms, 19.6MB)
# 테스트 11 〉	통과 (2821.04ms, 19.8MB)
# 테스트 12 〉	통과 (774.44ms, 14.8MB)
# 테스트 13 〉	통과 (921.61ms, 14.6MB)
# 테스트 14 〉	통과 (993.98ms, 14.7MB)
# 테스트 15 〉	통과 (1058.15ms, 14.7MB)
# 테스트 16 〉	통과 (59.05ms, 10.4MB)
# 테스트 17 〉	통과 (36.05ms, 10.2MB)
# 테스트 18 〉	통과 (63.37ms, 10.2MB)
# 테스트 19 〉	통과 (94.39ms, 10.6MB)
# 테스트 20 〉	통과 (251.87ms, 11MB)
# 테스트 21 〉	통과 (125.74ms, 10.9MB)
# 테스트 22 〉	통과 (1194.79ms, 14.8MB)
# 테스트 23 〉	통과 (672.61ms, 14.8MB)
# 테스트 24 〉	통과 (1255.32ms, 14.9MB)
# 테스트 25 〉	통과 (36.80ms, 10.2MB)
# 테스트 26 〉	통과 (31.31ms, 10.3MB)
# 테스트 27 〉	통과 (179.65ms, 10.6MB)
# 테스트 28 〉	통과 (186.84ms, 10.7MB)
# 테스트 29 〉	통과 (14.45ms, 10.4MB)
# 테스트 30 〉	통과 (12.40ms, 10.3MB)