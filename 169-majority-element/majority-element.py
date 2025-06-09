class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        b=len(nums)
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
            if a[i]>b//2:
                return i

        