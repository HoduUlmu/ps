def solution(x, n):
    answer = [x + x * i for i in range(n)]
    return answer


solution(2, 5)
solution(4, 3)
solution(-4, 2)
solution(0, 5)