class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        word = ""
        for char in s:
            if char.isalpha() or char.isdigit(): word += char
            elif word:
                words.append(word)
                word = ""
        
        if word: words.append(word)
        return " ".join(reversed(words))

print(Solution().reverseWords(s = "the sky is blue"))
print(Solution().reverseWords(s = "  hello world  "))
print(Solution().reverseWords(s = "a good   example"))
print(Solution().reverseWords(s = "  Bob    Loves  Alice   "))
print(Solution().reverseWords(s = "Alice does not even like bob"))
print(Solution().reverseWords(s = "A"))
        