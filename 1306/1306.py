from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = [False] * len(arr)
        visitCount = 0
        numStack = [start]

        while visitCount != len(arr) and numStack:
            currentPos = numStack.pop(0)
            if not visit[currentPos]:
                visitCount += 1
                visit[currentPos] = True

                if not arr[currentPos]: return True

                aheadPos = currentPos + arr[currentPos]
                behindPos = currentPos - arr[currentPos]

                if aheadPos <= len(arr) - 1 and not visit[aheadPos]: numStack.append(aheadPos)
                if behindPos >= 0 and not visit[behindPos]: numStack.append(behindPos)

        return False

print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5))
print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(Solution().canReach(arr = [3,0,2,1,2], start = 2))
print(Solution().canReach(arr = [0,1], start = 1))

