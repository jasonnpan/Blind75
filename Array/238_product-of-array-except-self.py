# 238. Product of Array Except Self
# LeetCode Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        suffix = 1
        for n in range (len(nums)):
            answer[n] *= prefix
            prefix *= nums[n]
        for n in range (len(nums) - 1, -1, -1):
            answer[n] *= suffix
            suffix *= nums[n]
        
        return answer
