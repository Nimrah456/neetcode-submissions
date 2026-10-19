class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        while right - left + 1 > k:#bcz we need to check until we get exctly k elements the moment we have equal to k itll hit false and then give us the result
            if abs(arr[left] - x) < abs(arr[right] - x) or abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
                right -= 1
            else:
                left += 1
        return arr[left:right+1]            

        