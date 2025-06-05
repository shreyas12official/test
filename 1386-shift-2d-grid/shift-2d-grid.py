class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k %= total
        flat = flat[-k:] + flat[:-k]
        return [[flat[i * n + j] for j in range(n)] for i in range(m)]