def solution(s: str):
    idx, ans = 0, []
    for char in s:
        if char.isspace():
            ans.append(char)
            idx = 0
        else:
            ans.append(char.upper() if not idx % 2 else char.lower())
            idx += 1
    return ''.join(ans)


print(solution("try hello"))
print(0 % 2 == 0)

# def toWeirdCase(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
