from typing import List


def solution(lottos: List, win_nums: List) -> List[int]:
    lottos.sort()
    win_nums.sort()

    correct_num = zero_num = 0

    while lottos:
        top = lottos.pop()

        if top == 0:
            zero_num += len(lottos) + 1
            break

        if top > win_nums[-1]:
            continue
        elif top < win_nums[-1]:
            win_nums.pop()
            lottos.append(top)
        else:
            win_nums.pop()
            correct_num += 1

    rank = 6 if correct_num == 0 else 6 - correct_num + 1
    zero_num = 5 if zero_num == 6 else zero_num
    result = [rank - zero_num, rank]
    return result


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([3, 4, 5, 8, 2, 7], [31, 10, 45, 40, 41, 19]))
print(solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 40, 41, 19]))
print(solution([0, 0, 0, 0, 0, 1], [31, 10, 45, 40, 41, 19]))
