def solution(n):
    return sum(int(i) for i in str(n))


print(solution(0))

# 재귀적
# def sum_digit(number):
#     if number < 10:
#         return number;
#     return (number % 10) + sum_digit(number // 10)
