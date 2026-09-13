class Solution:
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      maxl = 0
      maxr = 0
      water = 0
      while left < right:
        if height[left] <= height[right]:
          #we proceed left bcz left is smaller and that determines the water amt
          if height[left] >= maxl:
            #nowater
            maxl = height[left]
          else:
            water +=  maxl - height[left]
          left +=1 
        else:
          if height[right] <= height[left]:
          #we proceed right bcz right is smaller and that determines the water amt
            if height[right] >= maxr:
              #nowater
              maxr = height[right]
            else:
              water +=  maxr - height[right]
            right -=1
      return water     




        