# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         result = [1 for i in range(5)]
#         while n > 1:
#             for i in range(3, -1, -1):
#                 result[i] = result[i + 1] + result[i]
#             n -= 1

#         return  sum(result)

# Solution from lee
class Solution:
    def countVowelStrings(self, n):
        seen = {}
        def dp(n, k):
            if k == 1 or n == 1: return k
            if (n, k) in seen:
                return seen[n, k]
            seen[n, k] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[n, k]
        return dp(n, 5)

# print(Solution().countVowelStrings(1))
print(Solution().countVowelStrings(2))
# print(Solution().countVowelStrings(33))

# testDict = {3:4, 4:5, 4:5, (4, 5): 4}
# print(sum(testDict))
# print((4, 5) in testDict)