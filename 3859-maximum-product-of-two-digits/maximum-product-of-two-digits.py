class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        for d in str(n):
            digits.append(int(d)) 
        max_product = 0
        for i in range(len(digits)):
            for j in range(i, len(digits)): 
                product = digits[i] * digits[j]
                if i == j and digits.count(digits[i])<2:
                    continue
                if product > max_product:
                    max_product = product
        return max_product
        