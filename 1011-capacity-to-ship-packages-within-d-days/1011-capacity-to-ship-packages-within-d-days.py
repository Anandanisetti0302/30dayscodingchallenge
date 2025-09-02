class Solution(object):
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            total, required_days = 0, 1
            for w in weights:
                if total + w > mid:
                    required_days += 1
                    total = 0
                total += w
            if required_days > days:
                left = mid + 1
            else:
                right = mid
        return left

        