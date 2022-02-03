def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(["sun", "bed", "car"], 2))
print(solution(["abce", "abcd", "cdx"], 2))
print(solution(["abce", "abcd", "cdx"], 2))
