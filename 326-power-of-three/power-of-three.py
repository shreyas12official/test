class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        largest_power_of_three = 1162261467
        if largest_power_of_three % n == 0:
            return True
        else:
            return False