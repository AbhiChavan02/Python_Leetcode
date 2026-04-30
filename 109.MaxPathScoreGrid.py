class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        INF = float("-inf")
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == INF:
                        continue

                    # Move Down
                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost],
                                dp[i][j][c] + val
                            )

                    # Move Right
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j][c + cost] = max(
                                dp[i][j][c + cost],
                                dp[i][j][c] + val
                            )

        ans = max(dp[m - 1][n - 1])
        return -1 if ans < 0 else ans


m, n, k = map(int, input("Enter m n k: ").split())

grid = []
print("Enter grid rows:")
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

sol = Solution()
result = sol.maxPathScore(grid, k)

print("Maximum Path Score:", result)

# 3 3 2
# 0 1 2
# 3 0 4
# 5 6 0
# -> -1