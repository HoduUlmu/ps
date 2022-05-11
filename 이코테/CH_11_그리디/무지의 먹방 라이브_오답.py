# 정확성 테스트 통과

def solution(food_times: list, k: int):
    length = len(food_times)
    if length > k:
        return k + 1

    if sum(food_times) <= k:
        return -1

    time = 0
    eat = 0

    while time < k:
        while food_times[eat] == 0:
            eat = eat + 1 if eat < length - 1 else 0
        food_times[eat] -= 1
        eat = eat + 1 if eat < length - 1 else 0
        time += 1

    while food_times[eat] == 0:
        eat = eat + 1 if eat < length - 1 else 0

    return eat + 1


print(solution([3, 1, 2], 5))

