def solution(left, right):
    ans = []
    for i in range(left, right + 1):
        temp = 0
        for j in range(1, i + 1):
            if not i % j:
                temp += 1
        ans.append(i if not temp % 2 else -i)
    return sum(ans)


print(solution(13, 17))


# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer