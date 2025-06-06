class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a = 0
        b = len(mat)
        for i in range(b):
            for j in range(b):
                if i == j or i + j == b - 1:
                    a += mat[i][j]
        
        return a

        

        