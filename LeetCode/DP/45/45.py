from typing import List

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         lastIndex = len(nums) - 1
#         stepCount = 0

#         while lastIndex != 0:
#             for i in range(0, lastIndex):
#                 if i + nums[i] >= lastIndex:
#                     stepCount += 1
#                     lastIndex = i
#                     break

#         return stepCount


# Another solution base on greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = curEnd = curFarthest = 0

        for i in range(0, len(nums)):
            curFarthest = max(curFarthest, i + nums[i])
            if curEnd == i:
                jumps += 1
                curEnd = curFarthest
        return jumps


print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))
print(Solution().jump([4, 3, 1]))
print(Solution().jump([0]))
