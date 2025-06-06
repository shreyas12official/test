class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        b = len(grid)
        c = []
        for i in range(b - 2):
            d = []
            for j in range(b - 2):
                e = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        e = max(e, grid[x][y])
                d.append(e)
            c.append(d)
        return c
        