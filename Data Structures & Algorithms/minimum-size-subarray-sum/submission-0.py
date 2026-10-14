class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        l = float('inf')
        s = 0
        for right in range(n):
            s += nums[right]
            while s >= target:
                window = right-left+1
                l = min(l,window)
                s -= nums[left]
                left += 1
        return 0 if l == float('inf') else l        





        