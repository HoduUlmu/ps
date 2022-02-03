from functools import cmp_to_key


def solution(files):
    answer = sorted(files, key=cmp_to_key(compare))
    return answer


def compare(f1: str, f2: str):
    f1, f2 = f1.lower(), f2.lower()
    f1_head, f2_head = get_head(f1), get_head(f2)
    if f1_head[0] > f2_head[0]:
        return 1
    elif f1_head[0] < f2_head[0]:
        return -1
    else:
        f1_num = get_num(f1_head[1], f1)
        f2_num = get_num(f2_head[1], f2)
        if f1_num > f2_num:
            return 1
        elif f1_num < f2_num:
            return -1
        else:
            return 0


def get_head(s: str):
    for idx, char in enumerate(s):
        if char.isdigit():
            return s[:idx], idx
    return s


def get_num(idx: int, s: str):
    s = s[idx:]
    for end, char in enumerate(s):
        if not char.isdigit():
            return int(s[:end])
    return int(s)


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img13123"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "f010bar020.zip"])

# lock = False
# num_start = f1_number = f1_tail = f1_head = None
# for idx, char in enumerate(f1):
#     if not lock and char.isdigit():
#         f1_head = f1[:idx]
#         num_start = idx
#         lock = True
#     if lock and not char.isdigit():
#         f1_number = int(f1[num_start:idx])
#         f1_tail = f1[idx:]
#         break
# if not num_start:
#     f1_head = f1

# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (22.09ms, 10.6MB)
# 테스트 4 〉	통과 (31.09ms, 10.6MB)
# 테스트 5 〉	통과 (21.56ms, 10.6MB)
# 테스트 6 〉	통과 (23.32ms, 10.6MB)
# 테스트 7 〉	통과 (22.29ms, 10.6MB)
# 테스트 8 〉	통과 (25.51ms, 10.6MB)
# 테스트 9 〉	통과 (20.82ms, 10.6MB)
# 테스트 10 〉	통과 (20.58ms, 10.6MB)
# 테스트 11 〉	통과 (22.05ms, 10.6MB)
# 테스트 12 〉	통과 (38.43ms, 10.6MB)
# 테스트 13 〉	통과 (2.98ms, 10.7MB)
# 테스트 14 〉	통과 (3.43ms, 10.7MB)
# 테스트 15 〉	통과 (3.47ms, 10.7MB)
# 테스트 16 〉	통과 (22.55ms, 10.6MB)
# 테스트 17 〉	통과 (2.82ms, 10.6MB)
# 테스트 18 〉	통과 (11.51ms, 10.6MB)
# 테스트 19 〉	통과 (14.35ms, 10.6MB)
# 테스트 20 〉	통과 (14.32ms, 10.6MB)
