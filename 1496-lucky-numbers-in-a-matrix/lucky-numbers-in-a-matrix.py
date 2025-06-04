class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        c = []
        for i in range(len(matrix)):
            b = min(matrix[i])
            j = matrix[i].index(b)
            d = True
            for k in range(len(matrix)):
                if matrix[k][j] > b:
                    d = False
                    break
            if d:
                c.append(b)
        return c

        