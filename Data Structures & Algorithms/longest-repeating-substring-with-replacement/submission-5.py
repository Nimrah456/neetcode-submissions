class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)
        counts = [0]*26
        longest = 0
        for right in range(n):
            counts[ord(s[right]) - ord('A')] += 1
            while right - left + 1 - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest = max(right - left + 1,longest)
        return longest

        