class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.validate(a, b) or self.validate(b, a)

    def validate(self, a: str, b: str) -> bool:
        i = 0; j = len(a) - 1
        while i <= j and a[i] == b[j]:
            i = i + 1
            j = j -1
        if i >= j: return True
        return self.isPalindrome(i, b) or self.isPalindrome(i, a)

    def isPalindrome(self, left: int, s: str) -> bool:
        right = len(s) - 1 - left
        while left <= right and s[left] == s[right]:
            left = left + 1
            right = right - 1
        return left > right

print(Solution().checkPalindromeFormation(a = "x", b = "y"))
print(Solution().checkPalindromeFormation(a = "abdef", b = "fecab"))
print(Solution().checkPalindromeFormation(a = "ulacfd", b = "jizalu"))
print(Solution().checkPalindromeFormation(a = "xbdef", b = "xecab"))
print(Solution().checkPalindromeFormation(a = "pvhmupgqeltozftlmfjjde", b = "yjgpzbezspnnpszebzmhvp"))
print(Solution().checkPalindromeFormation(a = "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", b = "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))
print(Solution().checkPalindromeFormation(a = "abda", b = "acmc"))