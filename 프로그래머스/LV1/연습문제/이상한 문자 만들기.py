def solution(s: str):
    ans = []
    for words in s.split():
        for idx, char in enumerate(words):
            if idx == 0 or idx % 2 == 0:
                ans.append(char.upper())
            else:
                ans.append(char.lower())
        ans.append(" ")

    return


solution("try hello")
