def solution(triangle):

    for row in range(len(triangle) - 2, -1, -1):
        for idx in range(len(triangle[row])):
            triangle[row][idx] += max(triangle[row + 1][idx], triangle[row + 1][idx + 1])
    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])