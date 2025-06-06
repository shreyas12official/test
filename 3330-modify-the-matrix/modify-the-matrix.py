class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        b = len(matrix)
        c = len(matrix[0])
        d = []
        for j in range(c):
            e = 0
            for i in range(b):
                if matrix[i][j] > e:
                    e = matrix[i][j]
            d.append(e)
        for i in range(b):
            for j in range(c):
                if matrix[i][j] == -1:
                    matrix[i][j] = d[j]

        return matrix
        