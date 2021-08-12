# Brute force
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reveredStr = s[::-1]
        for i in range(0, len(s)):
            if s[:len(s) - i] == reveredStr[i:]:
                return s[len(s) - i:][::-1] + s

print(Solution().shortestPalindrome('aacecaaa'))