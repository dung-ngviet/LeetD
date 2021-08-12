class Solution:
    def climbStairs(self, n: int) -> int:
        steps_current = steps_previous = 1

        while n > 1:
            n -= 1
            steps_current = steps_current + steps_previous
            steps_previous = steps_current - steps_previous

        return steps_current

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))