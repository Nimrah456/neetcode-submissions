class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count= [0] * 26
        while len(s1) > len(s2):
            return False
        for right in range(len(s2)):
            count[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 > len(s1):
                count[ord(s2[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(s1):
                window = s2[left:right+1]
                if sorted(window) == sorted(s1):
                    return True
        return False     



    
    