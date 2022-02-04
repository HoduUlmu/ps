def solution(n):
    return sum(x for x in range(1, n + 1) if n % x == 0)


print(solution(12))
print(solution(5))
print(solution(0))