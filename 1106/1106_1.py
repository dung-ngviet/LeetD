class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1: return True if expression == 't' else False
        if expression[0] == '!': return not self.parseBoolExpr(expression[2:len(expression) - 1])
        isAnd = True if expression[0] == '&' else False
        if isAnd:
            result = True
        else:
            result = False
        bracketsCount = 0
        startIndex = 2
        for i in range(2, len(expression)):
            c = expression[i]
            if c == '(': bracketsCount += 1
            if c == ')': bracketsCount -= 1

            if bracketsCount == 0 and c == ',' or i == len(expression) - 1:
                if isAnd:
                    result = result and self.parseBoolExpr(expression[startIndex:i])
                else: 
                    result = result or self.parseBoolExpr(expression[startIndex:i])
                startIndex = i + 1

        return result

print(Solution().parseBoolExpr('!(f)'))
print(Solution().parseBoolExpr('|(f,t)'))
print(Solution().parseBoolExpr('&(t,f)'))
print(Solution().parseBoolExpr('|(&(t,f,t),!(t))'))
print(Solution().parseBoolExpr('&(t,t,t)'))