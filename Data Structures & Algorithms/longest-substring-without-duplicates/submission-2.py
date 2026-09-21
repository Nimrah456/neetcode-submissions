class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ss = set()
        current = 0
        maximum = 0
        i = 0
        j = 0
        for i in range(n):
            if s[i] not in ss:
                ss.add(s[i])
                current = len(ss)
                if current > maximum:
                    maximum = current
                maximum = max(current,maximum)
            else:
                while s[i] in ss:
                    ss.remove(s[j])
                    j += 1
                ss.add(s[i])
                current = len(ss)
                if current > maximum:
                    maximum = current

        return maximum            
                

                    

            
        