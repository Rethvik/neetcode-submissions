class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        if(len(s) == 1 and len(t) == 1 and s == t):
            return True
        s_unique_values = set(s)
        for i in s_unique_values:
            if s.count(i) != t.count(i):
                return False
        return True
        