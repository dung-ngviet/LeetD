from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0 for i in range(len(nums))]
        self.sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.sum[i] = self.sum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right] - self.sum[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))