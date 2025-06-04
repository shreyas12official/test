class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = 0
        size = len(nums)
        for i in range(size):
            a = nums[i]
            if i - k >= 0:
                b = nums[i - k]
            else:
                b = None
            if i + k < size:
                c = nums[i + k]
            else:
                c = None
            is_good = True
            if b is not None and a <= b:
                is_good = False
            if c is not None and a <= c:
                is_good = False
            if is_good:
                result += a
        return result

        