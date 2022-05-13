def solution(answers):
    one_ans_num = len([x for x in range(len(answers)) if answers[x] == [1, 2, 3, 4, 5][x % 5]])
    two_ans_num = len([x for x in range(len(answers)) if answers[x] == [2, 1, 2, 3, 2, 4, 2, 5][x % 8]])
    three_ans_num = len([x for x in range(len(answers)) if answers[x] == [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][x % 10]])
    max_num = max(one_ans_num, two_ans_num, three_ans_num)
    return [x + 1 for x in range(3) if [one_ans_num, two_ans_num, three_ans_num][x] == max_num]


print(solution([1, 2, 3, 4, 5, 1, 3, 2, 4, 2]))
print(solution([1, 3, 2, 4, 2]))

# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0] * len(p)
#
#     for q, a in enumerate(answers):
#         for i, v in enumerate(p):
#             if a == v[q % len(v)]:
#                 s[i] += 1
#     return [i + 1 for i, v in enumerate(s) if v == max(s)]

# cycle 존재함
# from itertools import cycle
#
# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)
#
#     return [i + 1 for i, v in enumerate(scores) if v == highest]