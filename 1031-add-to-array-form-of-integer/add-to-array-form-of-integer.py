class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        result = []
        carry = k
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
            result.append(carry % 10)
            carry //= 10
            i -= 1
        result.reverse()
        return result
