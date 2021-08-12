from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefixArray = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        answer = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                prefixPreviousCol = 0 if j == 0 else prefixArray[i][j - 1]
                prefixPreviousRow = 0 if i == 0 else prefixArray[i - 1][j]
                prefixPreviousBoth = 0 if i == 0 or j == 0 else prefixArray[i - 1][j - 1]
                prefixArray[i][j] = prefixPreviousCol + prefixPreviousRow - prefixPreviousBoth + mat[i][j]

        rows = len(mat)
        cols = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                bottom = i + k if i + k < rows else rows - 1
                right = j + k if j + k < cols else cols - 1
                top = i - k if i - k >= 0 else 0
                left = j - k if j - k > 0 else 0
                
                if top == 0 and left != 0: answer[i][j] = prefixArray[bottom][right] - prefixArray[bottom][left - 1]
                elif top != 0 and left == 0: answer[i][j] = prefixArray[bottom][right] - prefixArray[top - 1][right]
                elif top != 0 and left != 0: answer[i][j] = prefixArray[bottom][right] - prefixArray[bottom][left - 1] - prefixArray[top - 1][right] + prefixArray[top - 1][left - 1]
                else: answer[i][j] = prefixArray[bottom][right]


        return answer

print(Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2))
