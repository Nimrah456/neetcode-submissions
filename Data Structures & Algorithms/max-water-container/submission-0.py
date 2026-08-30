class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        maxarea = 0
        while i < j:
            width = j - i
            length = min(heights[i],heights[j])
            a = width * length
            maxarea = max(maxarea, a)
            if heights[j] < heights[i]:
                j-=1
            else:
                i+=1
        return maxarea            




            
            


            
            
            

        

        