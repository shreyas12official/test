class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        a=0
        b=0
        for i in nums:
            temp=max(a,b+i)
            b=a
            a=temp
        return a

                      
          
        