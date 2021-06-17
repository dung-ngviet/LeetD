class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balancedStrCount = 0
        lCount = rCount = 0
        for i in range(len(s)):
            lCount = lCount + 1 if s[i] == 'L' else lCount
            rCount = rCount + 1 if s[i] == 'R' else rCount
            if rCount == lCount:
                balancedStrCount = balancedStrCount + 1
                lCount = 0
                rCount = 0

        return balancedStrCount

print(Solution().balancedStringSplit('RLRRLLRLRL'))
print(Solution().balancedStringSplit('RLLLLRRRLR'))
print(Solution().balancedStringSplit('LLLLRRRR'))
print(Solution().balancedStringSplit('RLRRRLLRLL'))
