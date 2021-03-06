def solution(s):
    ans = len(s)

    for divisor in range(1, len(s) // 2 + 1):
        fp = sp = 0
        short_s = prev = ''
        count = 1
        while fp < len(s):
            sp += divisor
            now = s[fp: sp]

            if prev == now:
                count += 1
                if sp >= len(s):
                    short_s += (str(count) + prev)
            else:
                if count > 1:
                    short_s += (str(count) + prev)
                else:
                    short_s += prev
                if sp >= len(s):
                    short_s += now
                if len(short_s) >= ans:
                    break
                count = 1

            fp = sp
            prev = now

        ans = min(ans, len(short_s))

    return ans


print(solution("caacaabd"))
#
# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.26ms, 10.2MB)
# 테스트 3 〉	통과 (0.11ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.1MB)
# 테스트 7 〉	통과 (0.76ms, 10.2MB)
# 테스트 8 〉	통과 (0.52ms, 10.3MB)
# 테스트 9 〉	통과 (1.11ms, 10.2MB)
# 테스트 10 〉	통과 (1.92ms, 10.2MB)
# 테스트 11 〉	통과 (0.16ms, 10.2MB)
# 테스트 12 〉	통과 (0.18ms, 10.3MB)
# 테스트 13 〉	통과 (0.10ms, 10.4MB)
# 테스트 14 〉	통과 (0.51ms, 10.2MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (1.02ms, 10.3MB)
# 테스트 18 〉	통과 (1.85ms, 10.3MB)
# 테스트 19 〉	통과 (1.26ms, 10.2MB)
# 테스트 20 〉	통과 (2.44ms, 10.2MB)
# 테스트 21 〉	통과 (3.28ms, 10.2MB)
# 테스트 22 〉	통과 (2.58ms, 10.2MB)
# 테스트 23 〉	통과 (2.26ms, 10.2MB)
# 테스트 24 〉	통과 (3.40ms, 10.3MB)
# 테스트 25 〉	통과 (2.81ms, 10.2MB)
# 테스트 26 〉	통과 (4.09ms, 10.4MB)
# 테스트 27 〉	통과 (4.16ms, 10.3MB)
# 테스트 28 〉	통과 (0.03ms, 10.2MB)