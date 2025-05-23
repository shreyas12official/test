class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split()
        r = list(l[:k])
        new = " ".join(r)
        return new


      