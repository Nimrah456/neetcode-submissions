from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ama = defaultdict(list)
        for s in strs:
            count = [0]*26
            for a in s:
                count[ord(a) - ord('a')]+=1
            key = tuple(count)
            ama[key].append(s)
        return list(ama.values())    
        

            
    

                
        