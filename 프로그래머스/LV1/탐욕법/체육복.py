def solution(n, lost, reserve):
    dupl = [x for x in lost if x in reserve]
    lost = sorted([x for x in lost if x not in dupl])
    reserve = [x for x in reserve if x not in dupl]

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            n -= 1
    return n


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [3]))
