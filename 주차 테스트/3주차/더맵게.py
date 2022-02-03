import heapq


def solution(scoville, K):
    count = 0
    min_scoville = min(scoville)
    if min_scoville >= K:
        return count

    heapq.heapify(scoville)

    while len(scoville) > 1:
        least_not_hot = heapq.heappop(scoville)
        second_not_hot = heapq.heappop(scoville)
        mix = least_not_hot + second_not_hot * 2
        
        if scoville:
            min_scoville = min(mix, scoville[0])
        else:
            min_scoville = mix

        heapq.heappush(scoville, mix)
        count += 1
        if min_scoville >= K:
            return count

    return -1


solution([1, 2, 3, 9, 10, 12], 7)
print(solution([1, 2, 3, 9, 10, 12], 2000000000))
#
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.53ms, 10.2MB)
# 테스트 7 〉	통과 (0.44ms, 10.3MB)
# 테스트 8 〉	통과 (0.09ms, 10.3MB)
# 테스트 9 〉	통과 (0.09ms, 10.3MB)
# 테스트 10 〉	통과 (0.39ms, 10.2MB)
# 테스트 11 〉	통과 (0.23ms, 10.4MB)
# 테스트 12 〉	통과 (0.82ms, 10.2MB)
# 테스트 13 〉	통과 (0.44ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.3MB)
# 테스트 15 〉	통과 (0.58ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (188.11ms, 16.3MB)
# 테스트 2 〉	통과 (424.94ms, 22MB)
# 테스트 3 〉	통과 (2178.71ms, 49.8MB)
# 테스트 4 〉	통과 (146.84ms, 15MB)
# 테스트 5 〉	통과 (2231.05ms, 51.9MB)
