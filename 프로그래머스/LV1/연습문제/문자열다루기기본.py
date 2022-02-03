def solution(s: str):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


print(solution("a1234"))
print(solution("1234"))