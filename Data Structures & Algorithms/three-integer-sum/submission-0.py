class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)

        s = set()

        result = []

        for i in range(n):

            j = i + 1
            k = n - 1

            while j < k:

                addition = nums[j] + nums[k]

                if nums[i] + addition == 0:

                    t = (nums[i], nums[j], nums[k])

                    if t not in s:
                        s.add(t)
                        result.append(list(t))

                    j += 1
                    k -= 1

                elif nums[i] + addition < 0:
                    j += 1

                else:
                    k -= 1

        return result