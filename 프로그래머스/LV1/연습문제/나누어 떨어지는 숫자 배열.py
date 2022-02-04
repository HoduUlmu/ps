def solution(arr, divisor):
    ans = sorted(x for x in arr if x % divisor == 0)
    return ans if ans else [-1]


print(solution([5,9,7,10], 5))
print(solution([5,9,7,10], 200))

# 다른 분 코드
# def solution(arr, divisor):
#   return sorted([n for n in arr if n%divisor == 0]) or [-1]