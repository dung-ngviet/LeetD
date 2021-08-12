from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        charsS = defaultdict(int)
        charsT = defaultdict(int)
        for (sChar, tChar) in zip(s, t):
            charsS[sChar] += 1
            charsT[tChar] += 1
        stepNumbers = 0
        for char in charsS:
            delta = charsT[char] - charsS[char]
            if delta < 0: stepNumbers += delta
        return abs(stepNumbers)

print(Solution().minSteps(s = "bab", t = "aba"))
print(Solution().minSteps(s = "leetcode", t = "practice"))
print(Solution().minSteps(s = "anagram", t = "mangaar"))
print(Solution().minSteps(s = "xxyyzz", t = "xxyyzz"))
print(Solution().minSteps(s = "friend", t = "family"))