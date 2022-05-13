def solution(numbers):
    ans = []
    for idx, num in enumerate(numbers):
        for j in range(idx + 1, len(numbers)):
            if num + numbers[j] not in ans:
                ans.append(num + numbers[j])
    return sorted(ans)


print(solution([2, 1, 3, 4, 1]))

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))
