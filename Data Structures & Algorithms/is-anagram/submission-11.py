class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        e = sorted(s)
        f = sorted(t)
        if e == f:
            return True
        else:
            return False    
        