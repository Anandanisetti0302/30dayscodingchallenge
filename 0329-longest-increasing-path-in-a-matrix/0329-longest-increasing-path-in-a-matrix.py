class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]
            val = matrix[x][y]
            ans = 1
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > val:
                    ans = max(ans, 1 + dfs(nx, ny))
            dp[x][y] = ans
            return ans
        return max(dfs(i, j) for i in range(m) for j in range(n))

        