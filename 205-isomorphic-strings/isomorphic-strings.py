class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        pattern_a = []
        pattern_b = []
        for ch in s:
            pattern_a.append(s.index(ch))
        for ch in t:
            pattern_b.append(t.index(ch))
        return pattern_a == pattern_b
        