def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


# def solution(n):
#     for i in range(2, (n-1//2) +1) : #2부터~반값까지
#         if (n-1) % i == 0: #약수가 있다면
#             return i
#     return n - 1

print(solution(10))
