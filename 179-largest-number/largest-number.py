class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a=[]
        for i in nums:
            a.append(str(i))
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]+a[j]<a[j]+a[i]:
                    a[i],a[j]=a[j],a[i]
        b=''.join(a)
        if b[0]=='0':
            return str(0)
        return b


        