class Solution:
    def reverseString(self, s: List[str]) -> None:

        l = 0
        r = len(s) - 1
        
        while l < r:
            # Swap characters in-place
            s[l], s[r] = s[r], s[l]
            # Move pointers closer to the center
            l += 1
            r -= 1
