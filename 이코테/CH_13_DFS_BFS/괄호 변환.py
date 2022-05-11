import collections


def solution(p):
    def recursive(s: str, res):
        if len(s) == 0:
            return res

        q = collections.deque(s)
        u = collections.deque()
        left, num = 0, 0
        is_right = True

        while q:
            u.append(q.popleft())
            if u[-1] == ')':
                num += 1
                if left - 1 < 0:
                    is_right = False
                left -= 1
            else:
                num -= 1
                left += 1

            if num == 0:
                v = ''.join(q)

                if is_right:
                    res = ''.join(u) + recursive(v, res)
                    return res
                else:
                    res = '(' + recursive(v, res)
                    u.popleft(), u.pop()
                    u = ['(' if x == ')' else ')' for x in u]
                    res += ')' + ''.join(u)
                    return res

    if len(p) == 0:
        return ""

    return recursive(p, '')


print(solution("()))((()"))

# def check(s):
#     opened = 0
#     for each in s:
#         if each == '(':
#             opened += 1
#         else:
#             if opened:
#                 opened -= 1
#             else:
#                 return False
#     return True
#
#
# def separate(s):
#     opened = 0
#     for idx in range(len(s)):
#         if s[idx] == '(':
#             opened += 1
#         else:
#             opened -= 1
#         if not opened:
#             return (s[:idx+1], s[idx+1:])
#
#
# def solution(s):
#     if s:
#         u, v = separate(s)
#         if check(u):
#             return u+solution(v)
#         else:
#             temp = '(' + solution(v) + ')' + \
#                 ''.join('(' if i == ')' else ')' for i in u[1:-1])
#             return temp
#     else:
#         return ''
#
#
# assert(solution("(()())()") == "(()())()")
# assert(solution(")(") == "()")
# assert(solution("()))((()") == "()(())()")
