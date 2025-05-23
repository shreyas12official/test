class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original=original*2
        return original
        if original not in nums:
            return original
                
        