# 152. Maximum Product Subarray
# LeetCode Medium

# Given an integer array nums, find a subarray that has the largest product, and return the product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMin = 1
        curMax = 1
        for n in nums:
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            ans = max(curMax, ans)
        return ans
