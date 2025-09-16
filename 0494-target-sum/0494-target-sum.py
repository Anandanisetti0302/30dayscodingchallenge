class Solution(object):
    def findTargetSumWays(self, nums, target):
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for summ in dp:
                next_dp[summ + num] += dp[summ]
                next_dp[summ - num] += dp[summ]
            dp = next_dp
        return dp[target]

        