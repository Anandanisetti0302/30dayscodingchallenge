class Solution(object):
    def splitArray(self, nums, k):
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            total, count = 0, 1
            for num in nums:
                if total + num > mid:
                    count += 1
                    total = 0
                total += num
            if count > k:
                left = mid + 1
            else:
                right = mid
        return left

        