class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(nums)
        nums[:] = sorted(a)
        k = len(a)
        return k        