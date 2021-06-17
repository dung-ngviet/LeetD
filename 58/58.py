class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastChar = len(s) - 1
        while s[lastChar] == ' ': 
            lastChar -= 1
            if lastChar < 0: return 0

        charsCount = 0
        while s[lastChar].isalpha():
            lastChar -= 1
            charsCount += 1
            if lastChar < 0: return charsCount
        return charsCount

print(Solution().lengthOfLastWord(s = "Hello World"))
print(Solution().lengthOfLastWord(s = " "))
print(Solution().lengthOfLastWord(s = "a"))