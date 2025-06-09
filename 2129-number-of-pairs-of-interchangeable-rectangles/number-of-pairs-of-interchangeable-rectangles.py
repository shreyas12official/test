from math import gcd
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        a={}
        b=0
        for c,d in rectangles:
            e=gcd(c,d)
            s=(c//e,d//e)
            if s in a:
                b+=a[s]
                a[s]+=1
            else:
                a[s]=1
        return b