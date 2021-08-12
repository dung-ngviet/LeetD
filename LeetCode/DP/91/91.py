# My way to solve this problem
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         ways =  preWays = 0
#         for index in range(0, len(s)):
#             ch = s[index]
#             if index == 0:
#                 if ch == '0': return 0;
#                 ways = 1
#                 preWays = 1
#             else:
#                 twoLastChars = s[index-1] + ch
#                 twoLastCharsInt = int(twoLastChars, 10)
#                 if ch == '0':
#                     if self.isValidLetter(twoLastCharsInt):
#                         temp = ways
#                         ways = preWays
#                         preWays = temp
#                     else: return 0
#                 else:
#                     if self.isValidLetter(twoLastCharsInt):
#                         ways = ways + preWays
#                         preWays = ways - preWays
#                     else:
#                         preWays = ways
#         return ways

#     def isValidLetter(self, digits: int) -> bool:
#         return digits >= 10 and digits <= 26

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0 for x in range(len(s) + 1)]
        dp[0:2] = [1,1]

        for i in range(2, len(dp)):
            if 0 < int(s[i-1]) <= 9:
                dp[i] = dp[i - 1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("0"))
print(Solution().numDecodings("06"))
print(Solution().numDecodings("1111"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("27"))
print(Solution().numDecodings("10011"))
print(Solution().numDecodings("30"))
                    
                    
