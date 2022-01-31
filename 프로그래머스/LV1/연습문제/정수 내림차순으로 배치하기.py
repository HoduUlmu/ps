def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))

# 다른분 풀이
# def solution(n):
#     return int(''.join(sorted(str(n), reverse=True)))


