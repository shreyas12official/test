class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        r = [""] * len(a)
        for i in a:
            s = int(i[-1]) - 1
            r[s] = i[:-1]
        return " ".join(r)