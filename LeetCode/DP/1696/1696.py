from typing import List

class Solution:
    def maxResult(self, numss: List[int], ks: int) -> int:
        k = 70000
        nums = [-1 for i in range(0, 100000)]

        lastMaxSumIdx = 0
        maxSums = [nums[0] for i in range(len(nums))]

        for i in range(1, len(nums)):
            maxSums[i] = maxSums[lastMaxSumIdx] + nums[i]

            if nums[i] >= 0:
                lastMaxSumIdx = i
            else:
                if i - lastMaxSumIdx >= k:
                    temp = lastMaxSumIdx + 1
                    for j in range(lastMaxSumIdx + 1, i + 1):
                        if maxSums[j] >= maxSums[temp]: temp = j
                    lastMaxSumIdx = temp

        return maxSums[-1]

print(Solution().maxResult([1,-1,-2,4,-7,3], 2))
# print(Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3))
# print(Solution().maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))