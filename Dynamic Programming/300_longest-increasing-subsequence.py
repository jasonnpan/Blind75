# 300. Longest Increasing Subsequence
# LeetCode Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for a in range(len(nums) - 1, -1, -1):
            for b in range(a + 1, len(nums)):
                if (nums[a] < nums[b]):
                    dp[a] = max(dp[a], dp[b] + 1)
        return max(dp)
