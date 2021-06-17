from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        deliOccurs = defaultdict(int)

        for delicious in deliciousness:
            power = 1
            for exponent in range(0, 22):
                ans += deliOccurs[power - delicious]
                power *= 2

            deliOccurs[delicious] += 1
        
        return ans % 1000000007

print(Solution().countPairs([1,3,5,7,9])) # 4
print(Solution().countPairs([1,1,1,3,3,3,7])) # 15
print(Solution().countPairs([1048576,1048576])) # 1