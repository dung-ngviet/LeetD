from typing import List

class Solution:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    temp  = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

        return arr

print(Solution().bubble_sort([6,5,4,3,2,1]))