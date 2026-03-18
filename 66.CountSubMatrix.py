class Solution:
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = 0
        
        px = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                px[i+1][j+1] = (
                    grid[i][j]
                    + px[i][j+1]
                    + px[i+1][j]
                    - px[i][j]
                )
                
                if px[i+1][j+1] <= k:
                    ans += 1
        
        return ans


# ---- Input Section ----
print("Enter rows and columns (m n):")
m, n = map(int, input().split())

print("Enter matrix values row by row:")
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print("Enter value of k:")
k = int(input())

# ---- Output Section ----
sol = Solution()
result = sol.countSubmatrices(grid, k)

print("Output:", result)


# 2 2
# 1 2
# 3 4
# 7
# -> 3