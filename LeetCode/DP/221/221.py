from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for l in range(cols):
                if matrix[r][l] == "1":
                    if r == 0 or l == 0: result = max(result, 1)
                    else:
                        max_len_square = min(int(matrix[r - 1][l]), int(matrix[r - 1][l - 1]), int(matrix[r][l - 1])) + 1
                        if max_len_square > result: result = max_len_square
                        matrix[r][l] = str(max_len_square)

        return result * result
# 4
print(Solution().maximalSquare(
    [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
))

# 1
print(Solution().maximalSquare(
    [["0","1"],["1","0"]]  
))

# 0
print(Solution().maximalSquare(
    [["0"]]  
))