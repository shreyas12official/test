class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            rem = columnNumber % 26
            char = chr(65 + rem)
            result = char + result
            columnNumber = columnNumber // 26
        return result

        