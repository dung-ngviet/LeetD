class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps_array = [[1] * n] * m
        
        for row in range(1, m):
            for col in range(1, n):
                steps_array[row][col] = steps_array[row - 1][col] + steps_array[row][col - 1]

        return steps_array[m-1][n-1]

print(Solution().uniquePaths(m = 3, n = 7))
print(Solution().uniquePaths(m = 7, n = 3))
print(Solution().uniquePaths(m = 3, n = 2))
print(Solution().uniquePaths(m = 3, n = 3))
