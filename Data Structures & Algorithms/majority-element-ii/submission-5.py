from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = Counter(nums)
        m = [i for i in c if c[i] > n/3]
        return m


    
        