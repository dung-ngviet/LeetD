from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        nums.sort()

        if sum % 3 == 0:
            return sum
        else:
            remainder = sum % 3
            otherRemainder = 3 - remainder
            lowestNumberSameRemainder = 0
            sumOfNumbersWithOtherRemainder = 0
            numbersWithOtherRemainderCount = 0

            i = 0
            while i < len(nums):
                if nums[i] % 3 == remainder and lowestNumberSameRemainder == 0: lowestNumberSameRemainder = nums[i]
                elif nums[i] % 3 == otherRemainder and numbersWithOtherRemainderCount <= 1:
                    numbersWithOtherRemainderCount += 1
                    sumOfNumbersWithOtherRemainder += nums[i]

                if numbersWithOtherRemainderCount == 2 and lowestNumberSameRemainder != 0: break
                i += 1

        if lowestNumberSameRemainder != 0 and numbersWithOtherRemainderCount == 2:
            return sum - min(lowestNumberSameRemainder, sumOfNumbersWithOtherRemainder)
        elif lowestNumberSameRemainder != 0:
            return sum - lowestNumberSameRemainder
        else:
            return sum - sumOfNumbersWithOtherRemainder


print(Solution().maxSumDivThree([1, 2, 3, 4, 4]))
print(Solution().maxSumDivThree([4]))
print(Solution().maxSumDivThree([3,6,5,1,8]))
print(Solution().maxSumDivThree([2,6,2,2,7]))
print(Solution().maxSumDivThree([972,944,817,475,436,623,900,268,25,263,627,799,38,943,968,17,813,139,772,333,498,593,567,556,550,40,4,862,915,935,366,253,994,893,47,211,332,854,73,694,37,63,789,785,419,129,170,404,854,424,712,784,539,697,478,978,509,76,528,65,194,352,986,713,730,223,858,366,71,18,60,8,835,70,349,905,446,593,909,592,95,280,900,887,303,245,612,708,7,58,564,577,718,410,512,637,535,432,332,770]))
