class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = sorted(s)
        m = sorted(t)
        if n == m:
            return True
        else:
            return False    
        