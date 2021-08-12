import itertools
from typing import List
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == "{":
                if level == 0:
                    start = i + 1
                level += 1
            elif c == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == "," and level == 0:
                groups.append([])
            elif c.isalpha() and level == 0:
                groups[-1].append([c])
        wordsSet = set()
        for group in groups:
            while len(group) > 1:
                lastGroup = group.pop()
                secondLastGroup = group.pop()
                temp = [i + j for i in secondLastGroup for j in lastGroup]
                group.append(temp)
            wordsSet.update(*group)
        
        return sorted(wordsSet)


            

# ["ac","ad","ae","bc","bd","be"]
print(Solution().braceExpansionII("{a,b}{c,{d,e}}"))

["a","ab","ac","z"]
print(Solution().braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
