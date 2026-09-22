class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(t)
        b = sorted(s)
        if a == b:
            return True
        else:
            return False
        
        