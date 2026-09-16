class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        l = 0

        for right in range(len(nums)):

            if right - l > k:
                w.remove(nums[l])
                l += 1

            if nums[right] in w:
                return True

            w.add(nums[right])

        return False