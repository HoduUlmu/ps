def solution(a, b):
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return day[(sum(mon[:a - 1]) + b) % 7]


print(solution(5, 24))