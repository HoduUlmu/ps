def solution(seoul: list):
    idx = seoul.index("Kim")
    return f"김서방은 {idx}에 있다"


solution(["jane", "Kim"])

# 다른 사람 풀이
# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))