class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: an array of 0 or 1 elements is already sorted
        if len(nums) <= 1:
            return nums
        
        # 1. Divide: Find the midpoint and split the array
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # 2. Conquer & Combine: Merge the two sorted halves
        return self.merge(left_half, right_half)
        
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        res = []
        i = j = 0
        
        # Compare elements from both halves and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                
        # Append any remaining elements left over from either side
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res
