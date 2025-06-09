class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                a.append(nums[i])
        return a

     
