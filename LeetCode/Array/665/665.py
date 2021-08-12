class Solution(object):
    def checkPossibility(self, nums):
        decreasingCount = 0
        maxTemp = -100000
        for idx in range(0, len(nums) - 1):
            if nums[idx] > nums[idx+1]:
                decreasingCount += 1
                
                if nums[idx + 1] < maxTemp:
                    nums[idx + 1] = nums[idx]
                else:
                    nums[idx] = maxTemp
                maxTemp = max(maxTemp, nums[idx])
            else:
                maxTemp = max(maxTemp, nums[idx])
                
            if decreasingCount >= 2:
                return False

        return True

print(Solution().checkPossibility([4,2,1]))
print(Solution().checkPossibility([3,4,2,3]))

print(Solution().checkPossibility([4,2,3]))
print(Solution().checkPossibility([5,7,1,8]))