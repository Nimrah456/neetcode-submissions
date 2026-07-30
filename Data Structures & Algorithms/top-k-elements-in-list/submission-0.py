from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         result = Counter(nums).most_common(k)
         
         return [r[0] for r in result]
     