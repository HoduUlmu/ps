def solution(num):
    def recursive(n, ans):
        if ans > 500 or n == 1:
            return -1 if ans > 500 else ans

        n = n // 2 if not n % 2 else 3 * n + 1
        return recursive(n, ans + 1)
    return recursive(num, 0)


print(solution(6))
print(solution(1))
print(solution(16))
print(solution(626331))
