# 70. Climbing Stairs
# LeetCode Easy

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n - 1):
            tmp = a
            a = a + b
            b = tmp
        return a
