class Solution(object):
    def uniquePaths(self, m, n):
        res = 1
        for i in range(1, min(m, n)):
            res = res * (m + n - 1 - i) // i
        return res

        