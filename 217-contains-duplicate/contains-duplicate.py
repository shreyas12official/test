class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False      

        