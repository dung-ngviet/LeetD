from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, mid = 0, len(nums) - 1, 0

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1

# 4
print(Solution().search([-1,0,3,5,9,12], 9))

# 2
print(Solution().search([-1,0,3,5,9,12], 2))

# 0
print(Solution().search([5], 5))
