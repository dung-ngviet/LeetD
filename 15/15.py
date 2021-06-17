from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            left, right = idx + 1, len(nums) - 1
            complement = -nums[idx]

            while left < right:
                if nums[left] + nums[right] == complement:
                    ans.append((nums[idx], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < complement:
                    left += 1
                else:
                    right -= 1
        return ans


print(Solution().threeSum([-1,0,1,2,-1,-4]))

print(Solution().threeSum([]))
