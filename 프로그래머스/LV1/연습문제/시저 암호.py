def solution(s, n):
    s = list(s)
    for idx, char in enumerate(s):
        if not char.isspace():
            if (char.isupper() and 64 < ord(char) + n < 91) or (char.islower() and 96 < ord(char) + n < 123):
                s[idx] = chr(ord(char) + n)
            else:
                s[idx] = chr(ord(char) + n - 26)
    return ''.join(s)


print(solution("K      z d asd sa     B", 25))
# def caesar(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
#         elif s[i].islower():
#             s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
#
#     return "".join(s)
