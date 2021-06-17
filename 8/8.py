import re
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        start = 0
        while start < len(s) and s[start] == ' ': 
            start += 1
            if start == len(s): return 0
        isPositive = True
        
        firstChar = s[start]
        if firstChar == '-':
            isPositive = False
            start += 1
        elif firstChar == '+': start += 1
        elif not firstChar.isdigit():
            return 0
        while start < len(s) and s[start] == '0': start += 1

        Max = pow(2, 31)
        
        end = start
        while end < len(s) and s[end].isdigit(): end += 1
        if end == start: return 0
        number = s[start:end]
        
        if isPositive:
            if self.compare(number, str(Max)) >= 0: return int(Max - 1)
            else: return int(number)
        else:
            if self.compare(number, str(Max)) > 0: return -int(Max)
            else: return -int(number)

    def compare(self, a: str, b: str) -> int:
        if len(a) > len(b): return 1
        elif len(a) < len(b): return -1
        else:
            for (aChar, bChar) in zip(a, b):
                if int(aChar) > int(bChar): return 1
                elif int(aChar) < int(bChar): return -1
            return 0

print(Solution().myAtoi("1"))
print(Solution().myAtoi(s = "   -42"))
print(Solution().myAtoi(s = "   -42"))
print(Solution().myAtoi(s = "4193 with words"))
print(Solution().myAtoi(s = "words and 987"))
print(Solution().myAtoi(s = "-91283472332"))
print(Solution().myAtoi(s = "  "))
print(Solution().myAtoi(s = ""))
print(Solution().myAtoi(s = "21474836460"))

        
        
        
