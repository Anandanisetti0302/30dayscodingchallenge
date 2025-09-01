class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))

        