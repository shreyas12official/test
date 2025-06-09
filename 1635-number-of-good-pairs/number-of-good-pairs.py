class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a={}
        b=0
        for i in nums:
            if i in a:
                b+=a[i]
                a[i]+=1
            else:
                a[i]=1
        return b