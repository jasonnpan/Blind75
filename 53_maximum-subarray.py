# 53. Maximum Subarray
# LeetCode Medium

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum
