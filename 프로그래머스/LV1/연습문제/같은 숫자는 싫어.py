def solution(arr):
    dup = arr[0]
    ans = [dup]
    for num in arr:
        if dup != num:
            dup = num
            ans.append(dup)
    return ans


print(solution([4, 3]))
print(solution([1, 1, 3, 3, 0, 1, 1]))

# 다른분 풀이인대 인상깊었다
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]:
#             print(a[-1:])
#             continue
#         a.append(i)
#     return a
#
# def no_continuous2(s):
#     return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]
#
#
# print(no_continuous2([1, 1, 3, 3, 0, 1, 1]))
