import math


def solution(n):
    return (math.sqrt(n) + 1) ** 2 if int(math.sqrt(n)) ** 2 == n else -1


solution(121)
solution(3)
print(solution(1))
print(solution(100))
print(solution(101))

#  1로 나눈 나머지 활용
# def nextSqure(n):
#     sqrt = n ** (1/2)
#
#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return 'no'