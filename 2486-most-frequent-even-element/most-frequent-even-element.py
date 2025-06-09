class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i % 2 == 0:
                if i in a:
                    a[i]+=1
                else:
                    a[i]=1
        if not a:
            return -1
        s=0
        t=0
        for i in a:
            if a[i]>s:
                s=a[i]
                t=i
            elif a[i]==s:
                if i<=t:
                    t=i
        return t
            
        