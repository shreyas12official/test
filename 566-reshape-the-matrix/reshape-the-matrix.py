class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        flat = []
        for row in mat:
            for num in row:
                flat.append(num)
        result = []
        index = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat[index])
                index += 1
            result.append(new_row)
        return result
        