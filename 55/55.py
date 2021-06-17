from typing import List
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         max = 0
#         for i in range(0, len(nums)):
#             if i > max: return False
#             num = nums[i]
#             if i + num > max: max = i + num
#             if max > len(nums): return True
#         return max >= len(nums) - 1

# Backtracking solution, try every steps
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         return self.canJumpFromPosition(0, nums)

#     def canJumpFromPosition(self, pos: int, nums: List[int]) -> bool:
#         if pos == len(nums) - 1: return True
#         maxPos = min(pos + nums[pos], len(nums) - 1)
#         for i in range(pos + 1, maxPos + 1):
#             if self.canJumpFromPosition(i, nums): return True
#         return False


# # Backtracking solution with momezation
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         return self.canJumpFromPosition(0, nums)

#     def canJumpFromPosition(self, pos: int, nums: List[int]) -> bool:
#         if pos == len(nums) - 1: return True
#         maxPos = min(pos + nums[pos], len(nums) - 1)
#         for i in range(pos + 1, maxPos + 1):
#             if self.canJumpFromPosition(i, nums): return True
#         return False

# Greedy solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        
        return lastIndex == 0


print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([0]))
print(Solution().canJump([2,0,0]))

            