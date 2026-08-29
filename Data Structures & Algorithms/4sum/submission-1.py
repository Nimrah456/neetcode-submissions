class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        result = []
        for i in range(n):
            for j in range(i+1 ,n):
                k = j + 1
                l = n -1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        q = (nums[i],nums[j],nums[k],nums[l])
                        if q not in seen:
                            seen.add(q)
                            result.append(list(q))

                        k +=1
                        l-=1
                    elif total < target:
                        k+=1
                    else:
                        l-=1
        return result                            






                        

        
    