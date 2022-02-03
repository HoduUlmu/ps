def solution(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1: len(s) // 2 + 1]


print(solution("abcde"))
print(solution("abcd"))

# 다른 사람 풀이 대단하다
# def string_middle(str):
#     return str[(len(str)-1)//2:len(str)//2+1]
#
# print(string_middle("powe"))