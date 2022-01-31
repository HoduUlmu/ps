def solution(arr1, arr2):
    ans = []
    for x1, x2 in zip(arr1, arr2):
        ans.append([y1 + y2 for y1, y2 in zip(x1, x2)])
    return ans


solution([[1], [2]], [[3], [4]])
solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])


# def sumMatrix(A,B):
#     return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]