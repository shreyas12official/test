class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return[]
        s=[]
        for i in range(m):
            r=original[i*n:(i+1)*n]
            s.append(r)
        return s
        