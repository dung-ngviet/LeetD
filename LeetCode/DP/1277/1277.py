from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
      result = 0
      rows = len(matrix)
      cols = len(matrix[0])

      for r in range(rows):
        for l in range(cols):
          if matrix[r][l] == 1:
            if r == 0 or l == 0:
                result += 1
            else:
                max_square = min(
                    matrix[r - 1][l], matrix[r - 1][l - 1], matrix[r][l - 1]) + matrix[r][l]
                result += max_square
                matrix[r][l] = max_square

      return result

# 15
print(Solution().countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))

# 7
print(Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))
