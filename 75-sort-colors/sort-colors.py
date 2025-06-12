class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a = nums.count(0)
        b = nums.count(1)
        c = nums.count(2)
        
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
            elif i < a + b:
                nums[i] = 1
            else:
                nums[i] = 2
        