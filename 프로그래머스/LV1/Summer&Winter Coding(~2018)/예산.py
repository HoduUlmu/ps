def solution(d, budget):
    d = sorted(d)
    ans = 0
    while d and budget >= d[0]:
        ans += 1
        budget -= d.pop(0)
    return ans


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))

# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)
