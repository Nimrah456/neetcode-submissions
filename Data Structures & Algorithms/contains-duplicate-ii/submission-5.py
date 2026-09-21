class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        seen = set()
        while i < len(nums):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

            if i >= k:
                seen.remove(nums[i-k])

            i+=1
        return False            
        