class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxv = -1
        for i in range(n-1,-1,-1):
            temp = maxv 
            maxv = max(maxv,arr[i])
            arr[i] = temp
        return arr


              

            



                                 