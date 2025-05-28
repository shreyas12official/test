class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num_str = str(n)
        digits = [int(d) for d in list(num_str)]
        len_digits = len(digits)
        
        ret_val = 0
        i = 0
        while (i < len_digits):
            ret_val += digits[i] if (i % 2 == 0) else - digits[i]
            i += 1

        return ret_val
        