# 유클리드 호제법 https://codingpractices.tistory.com/34
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y, gcd_val):
    return x * y // gcd_val


def solution(n, m):
    gcd_val = gcd(n, m)
    return [gcd_val, lcm(n, m, gcd_val)]


print(solution(3, 12))

# def solution(n, m):
#     gcd = lambda a,b : b if not a%b else gcd(b, a%b)
#     lcm = lambda a,b : a*b//gcd(a,b)
#     return [gcd(n, m), lcm(n, m)]
