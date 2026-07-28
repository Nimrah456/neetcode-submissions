class Solution:
    def reverseString(self, s: List[str]) -> None:

        left = 0
        right = len(s) - 1
        
        while left < right:
            # Swap characters in-place
            s[left], s[right] = s[right], s[left]
            # Move pointers closer to the center
            left += 1
            right -= 1
