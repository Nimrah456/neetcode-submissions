from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hash map to store prefix sum frequencies
        # Start with {0: 1} to handle subarrays starting from index 0
        prefix_sum_count = Counter({0: 1})
      
        # Initialize result counter and running prefix sum
        result = 0
        current_sum = 0
      
        # Iterate through each number in the array
        for n in nums:
            # Update the running prefix sum
            current_sum += n
          
            # Check if (current_sum - k) exists in our hash map
            # If it exists, it means there are subarrays ending at current index
            # whose sum equals k
            result += prefix_sum_count[current_sum - k]
          
            # Add current prefix sum to the hash map for future iterations
            prefix_sum_count[current_sum] += 1
      
        return result
