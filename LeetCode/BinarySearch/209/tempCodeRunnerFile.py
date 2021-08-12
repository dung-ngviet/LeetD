def sum(self, arr, start, end):
        total = 0
        for i in range(start, end + 1):
            total += arr[i]
        return total

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ans = 0
        left, right = 0, 0
        while left <= right:
            sumSubarray = self.sum(nums, left, right)
            
            if sumSubarray < s:
                if right < len(nums) - 1:
                    right += 1
                if right == len(nums) - 1 and self.sum(nums, left, right) < s:
                    break
            else:
                if ans == 0:
                    ans = right - left + 1
                else:
                    if ans > (right - left + 1): ans = right - left + 1
                left += 1
                if right == len(nums) - 1 and self.sum(nums, left, right) < s:
                    break

        return ans