class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        left = 0
        maxFreq = 0
        result = 0

        for right in range(len(s)):

            # Count the current character
            count[ord(s[right]) - ord('A')] += 1

            # Highest frequency in the current window
            maxFreq = max(
                maxFreq,
                count[ord(s[right]) - ord('A')]
            )

            # Current window length
            windowLength = right - left + 1

            # Characters that need to be replaced
            replacements = windowLength - maxFreq

            # If we need more than k replacements,
            # shrink the window
            if replacements > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            # Update answer
            result = max(result, right - left + 1)

        return result