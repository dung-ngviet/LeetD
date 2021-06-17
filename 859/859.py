class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            chars = set()
            for a in A:
                if a in chars:
                    return True
                chars.add(a)
            return False
        else:
            diffPairs = []
            for a, b in zip(A, B):
                if a != b: diffPairs.append((a, b))
                if len(diffPairs) > 2: return False
            return len(diffPairs) == 2 and diffPairs[0] == (diffPairs[1][::-1])


print(Solution().buddyStrings(A = "ab", B = "ba")) # True
print(Solution().buddyStrings(A = "ab", B = "ab")) # false
print(Solution().buddyStrings(A = "aa", B = "aa")) # true
print(Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")) # true
print(Solution().buddyStrings(A = "", B = "aa")) # false