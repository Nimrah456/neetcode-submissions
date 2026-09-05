class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the amount of water that can be trapped after raining.
      
        Args:
            height: List of non-negative integers representing elevation map
          
        Returns:
            Total amount of trapped rainwater
        """
        n = len(height)
      
        # Initialize arrays to store maximum height to the left and right of each position
        left_max = [0] * n
        right_max = [0] * n
      
        # Base cases: first element for left_max, last element for right_max
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
      
        # Fill left_max array: for each position, store the maximum height seen so far from the left
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
      
        # Fill right_max array: for each position, store the maximum height seen so far from the right
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
      
        # Calculate trapped water at each position
        # Water level at position i = min(left_max[i], right_max[i])
        # Trapped water = water level - height of bar at position i
        total_water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            total_water += water_level - height[i]
      
        return total_water
