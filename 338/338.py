from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for x in range(n + 1)]

        for i in range(1, n+1):
            result[i] = result[i // 2] + i % 2

        return result

# print(Solution().countBits(16))
# print(Solution().countBits(0))
# print(Solution().countBits(1))
print(1 + 5 & 7)