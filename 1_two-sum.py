# 1. Two Sum

# LeetCode Easy
# Array, Hash Table

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = []
        n = len(nums)

        for i in range(0, n):
            k = target - nums[i]
            if k in table:
                return [table.index(k), i]
            table.append(nums[i])
        return []
