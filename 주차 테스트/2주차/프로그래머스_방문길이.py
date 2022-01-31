# 굳이 딕셔너리 안만들고 세트로 처리해도 된다
import collections


def solution(dirs):
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    route = collections.defaultdict(set)
    cur = (0, 0)

    for control in dirs:
        to_x = cur[0] + move[control][0]
        to_y = cur[1] + move[control][1]

        if -5 <= to_x <= 5 and -5 <= to_y <= 5:
            to = (to_x, to_y)
            route[cur].add(to)
            route[to].add(cur)
            cur = to

    result = sum(len(val) for val in route.values()) // 2

    return result


solution('ULURRDLLU')
solution('LULLLLLLU')
#
# 테스트 1 〉	통과 (0.07ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.10ms, 10.3MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.07ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.3MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 테스트 11 〉	통과 (0.04ms, 10.2MB)
# 테스트 12 〉	통과 (0.08ms, 10.3MB)
# 테스트 13 〉	통과 (0.08ms, 10.3MB)
# 테스트 14 〉	통과 (0.08ms, 10.3MB)
# 테스트 15 〉	통과 (0.07ms, 10.2MB)
# 테스트 16 〉	통과 (0.28ms, 10.3MB)
# 테스트 17 〉	통과 (0.28ms, 10.3MB)
# 테스트 18 〉	통과 (0.30ms, 10.3MB)
# 테스트 19 〉	통과 (0.29ms, 10.2MB)
# 테스트 20 〉	통과 (0.52ms, 10.3MB)