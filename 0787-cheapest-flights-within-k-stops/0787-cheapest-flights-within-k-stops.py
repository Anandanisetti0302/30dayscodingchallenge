class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        import sys
        INF = sys.maxsize
        # Bellman-Ford, keep costs for k+1 rounds
        dp = [INF] * n
        dp[src] = 0
        for _ in range(k+1):
            temp = dp[:]
            for u, v, w in flights:
                if dp[u] != INF and dp[u] + w < temp[v]:
                    temp[v] = dp[u] + w
            dp = temp
        return dp[dst] if dp[dst] != INF else -1

        