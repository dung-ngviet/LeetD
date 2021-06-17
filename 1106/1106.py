class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        chars = list()
        for chr in expression:
            if chr == ')':
                hasTrue = hasFalse = False
                poppedChar = chars.pop()
                while poppedChar == 't' or poppedChar == 'f':
                    hasTrue = hasTrue or poppedChar == 't'
                    hasFalse = hasFalse or poppedChar == 'f'
                    poppedChar = chars.pop()

                if poppedChar == '&':
                    chars.append('f' if hasFalse else 't')
                if poppedChar == '|':
                    chars.append('t' if hasTrue else 'f')
                if poppedChar == '!':
                    chars.append('f' if hasTrue else 't')

            elif chr != ',' and chr != '(': chars.append(chr)

        return True if chars.pop() == 't' else False

print(Solution().parseBoolExpr('!(f)'))
print(Solution().parseBoolExpr('|(f,t)'))
print(Solution().parseBoolExpr('&(t,f)'))
print(Solution().parseBoolExpr('&(t,f)'))
print(Solution().parseBoolExpr('|(&(t,f,t),!(t))'))
                