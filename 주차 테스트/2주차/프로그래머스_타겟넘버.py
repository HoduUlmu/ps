# 처음에 멍청하게 for문을 씀
def solution(numbers, target):
    answer = 0

    def dfs(n, idx):
        nonlocal answer
        if idx == len(numbers):
            if n == target:
                answer += 1
            return

        dfs(n + numbers[idx], idx + 1)
        dfs(n - numbers[idx], idx + 1)

    dfs(0, 0)
    return answer


solution([1, 1, 1, 1, 1], 3)
# 테스트 1 〉	통과 (363.00ms, 10.2MB)
# 테스트 2 〉	통과 (335.15ms, 10.2MB)
# 테스트 3 〉	통과 (0.35ms, 10.3MB)
# 테스트 4 〉	통과 (1.32ms, 10.3MB)
# 테스트 5 〉	통과 (10.66ms, 10.2MB)
# 테스트 6 〉	통과 (0.68ms, 10.2MB)
# 테스트 7 〉	통과 (0.60ms, 10.2MB)
# 테스트 8 〉	통과 (2.64ms, 10.2MB)