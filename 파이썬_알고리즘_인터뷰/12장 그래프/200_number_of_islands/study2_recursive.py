# 324ms, 16.9MB
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def dfs_recursive(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            for i in range(4):
                dfs_recursive(r + dx[i], c + dy[i])
            return

        for r in range(rows):
            for c in range(cols):
                node = grid[r][c]
                if node != '1':
                    continue

                cnt += 1
                dfs_recursive(r, c)
        return cnt