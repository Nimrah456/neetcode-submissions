class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = sorted(t)
        d = sorted(s)
        if c == d:
            return True
        else:
            return False
        
        