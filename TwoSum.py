# solution using hash table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = []
        n = len(nums)

        for i in range(0, n):
            k = target - nums[i]
            if k in table:
                return [table.index(k), i]
            else:
                table.append(nums[i])
        return []
