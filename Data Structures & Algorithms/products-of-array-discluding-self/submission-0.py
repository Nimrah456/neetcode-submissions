import math
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        for i in range(n):
                pr = nums[:i] + nums[i+1:]
                prefix[i] = math.prod(pr)
        return prefix    

        