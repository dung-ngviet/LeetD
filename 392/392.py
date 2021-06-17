class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iS = iT = 0
        while iS < len(s) and iT < len(t):
            if s[iS] == t[iT]:
                iS += 1    
            iT += 1

        return iS == len(s)

print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))
print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))