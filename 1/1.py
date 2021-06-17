from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsPos = dict()
        for idx in range(len(nums)):
            num = nums[idx]
            if target - num in numsPos:
                return [numsPos[target - num], idx]
            else:
                numsPos[num] = idx

        return []
            
print(Solution().twoSum([2,7,11,15], 9))