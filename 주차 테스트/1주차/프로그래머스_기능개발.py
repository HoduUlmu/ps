import collections


def solution(progresses, speeds):
    answer = []
    left_progress = [100 - x for x in progresses]
    time_left = collections.deque()

    for pro, speed in zip(left_progress, speeds):
        _time = pro // speed
        if _time == pro / speed:
            time_left.append(_time)
        else:
            time_left.append(_time + 1)

    while time_left:
        distribution = time_left.popleft()
        num = 1

        if not time_left:
            answer.append(num)
            break

        while time_left and distribution >= time_left[0]:
            time_left.popleft()
            num += 1

        answer.append(num)

    return answer


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
