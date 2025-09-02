class Solution(object):
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            if total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right

        