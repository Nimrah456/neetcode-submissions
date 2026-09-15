class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for right in range(len(nums)):

            if right - l > k:
                window.remove(nums[l])
                l += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False