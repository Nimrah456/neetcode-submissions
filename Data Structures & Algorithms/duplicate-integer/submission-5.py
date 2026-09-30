from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in nums:
            if c[i] > 1:
                return True
        return False    

        