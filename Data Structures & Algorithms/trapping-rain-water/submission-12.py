class Solution:

  def trap(self, height: List[int]) -> int:
    left_ptr = 0
    right_ptr = len(height) - 1
    max_left = 0
    max_right = 0
    water = 0

    while left_ptr < right_ptr:
      if height[left_ptr] <= height[right_ptr]:
        if height[left_ptr] >= max_left:
          max_left = height[left_ptr]
        else:
          water += max_left - height[left_ptr]
        left_ptr += 1
      else:
        if height[right_ptr] >= max_right:
          max_right = height[right_ptr]
        else:
          water += max_right - height[right_ptr]
        right_ptr -= 1

    return water
