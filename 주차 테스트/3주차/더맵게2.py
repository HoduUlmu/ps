# 효율성 테스트 전부 실패
import heapq


def solution(scoville, K):
    count = 0
    if min(scoville) >= K:
        return count

    heapq.heapify(scoville)

    while len(scoville) > 1:
        least_not_hot = heapq.heappop(scoville)
        second_not_hot = heapq.heappop(scoville)
        mix = least_not_hot + second_not_hot * 2

        heapq.heappush(scoville, mix)
        count += 1
        if min(scoville) >= K:
            return count

    return -1