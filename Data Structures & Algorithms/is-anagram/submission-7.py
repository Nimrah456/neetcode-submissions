class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = sorted(s)
        d = sorted(t)
        if c == d:
            return True
        else:
            return False    
        