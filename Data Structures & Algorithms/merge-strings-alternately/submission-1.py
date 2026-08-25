class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        s = ""
        for i in range(min(m,n)):
            s += word1[i] + word2[i]
        if n > m:
            s += word1[m:]
        elif m > n:
            s += word2[n:]  
        return s          


        