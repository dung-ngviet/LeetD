# Output: [4,5,1,2,3]
print_ll(Solution().rotateRight(array_to_ll([1,2,3,4,5]), 2))

# Output: [2,0,1]
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 4))

# Output: [0,1,2]
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 0))
print_ll(Solution().rotateRight(array_to_ll([0,1,2]), 3))

# Output: []
print_ll(Solution().rotateRight(array_to_ll([]), 4))

# Output: [1]
print_ll(Solution().rotateRight(array_to_ll([1]), 4))
print_ll(Solution().rotateRight(array_to_ll([1]), 0))
